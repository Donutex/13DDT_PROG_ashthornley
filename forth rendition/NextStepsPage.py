"""This is the next steps page.

This page allows users to view AI-predicted next steps for what they should do
with each one of their items. There is also a map that shows helpful locations
around the Auckland area that may assist with the decluttering process.
"""
import customtkinter as ctk
import functions
import tkintermapview
import time
import random
ctk.set_default_color_theme("forth rendition/theme.json")

class NextStepsPage:
    def __init__(self, conn, username):
        """necessary initialization for the Next Steps page.

        this part runs immediately when a new NextStepsPage object is created.
        it sets up the database connection (self.conn), remembers who the user
        is (self.username), sets up the window(self.root), prevents attribute
        errors for the prediction_display and local_map attributes, and calls
        the method to create the widgets create_widgets()

        Args:
            conn (SQLite3 Connection): The database connection object.
        """
        self.conn = conn
        self.username = username
        self.root = ctk.CTk()
        self.root.title("Next Steps")
        self.root.resizable(True, True)
        self.prediction_display = None
        self.local_map = None
        self._create_widgets()

    def _create_widgets(self):
        """Create the widgets for the Next Steps page.
        """
        # =========== Frames ===========
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill="x")

        body_frame = ctk.CTkFrame(self.root)
        body_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # mimic “LabelFrame” by adding a label on top
        next_steps_label = ctk.CTkLabel(
            body_frame,
            text="Predicted Actions",
            font=("Arial", 15)
        )
        next_steps_label.pack(anchor="w", padx=10)
        next_steps_frame = ctk.CTkFrame(body_frame)
        next_steps_frame.pack(padx=10, pady=(0, 10), fill="x")

        helpful_locations_label = ctk.CTkLabel(
            body_frame,
            text="Helpful Locations",
            font=("Arial", 15)
        )
        helpful_locations_label.pack(anchor="w", padx=10)
        helpful_locations_frame = ctk.CTkFrame(body_frame)
        helpful_locations_frame.pack(
            padx=10,
            pady=(0, 10),
            fill="both",
            expand=True
        )

        # =========== Title Area ===========
        ctk.CTkButton(
            title_frame,
            text="← Back to Main Page",
            command=self._return_to_main
        ).pack(side="left", padx=10, pady=5)

        ctk.CTkLabel(
            title_frame, text="Like A Knife Through Clutter", 
            font=("Papyrus", 24)
        ).pack(side="right", padx=10, pady=5)

        ctk.CTkLabel(
            title_frame, text=f"{self.username}'s Next Steps!",
            font=("Arial", 15)
        ).pack(anchor="center", padx=5, pady=5)

        # =========== Predicted Steps Area ===========
        ctk.CTkLabel(
            next_steps_frame,
            text="Here you can find the predicted next steps"
            " for what you should do with your items!",
            wraplength=600,
        ).pack(anchor="center", padx=5, pady=5)

        ctk.CTkButton(
            next_steps_frame,
            text="Get Next Steps",
            command=self.show_ai_next_steps
        ).pack(padx=10, pady=5)

        # Textbox for predictions
        self.prediction_display = ctk.CTkTextbox(
            next_steps_frame,
            height=200,
            width=600,
            wrap="word"
        )
        self.prediction_display.pack(padx=10, pady=5)

        # placeholder for the loading label
        self.prediction_loading_label = ctk.CTkLabel(next_steps_frame, text="")
        self.prediction_loading_label.pack(padx=10, pady=5)

        # =========== Map Area ===========
        ctk.CTkLabel(
            helpful_locations_frame,
            text="Helpful Locations Near You:"
        ).pack(anchor="center", padx=5, pady=5)

        # the map
        self.local_map = tkintermapview.TkinterMapView(
            helpful_locations_frame, 
            width=helpful_locations_frame.winfo_width(),
            height=200,
            corner_radius=0
        )
        self.local_map.pack(padx=10, pady=10, fill="x", expand=True)
        self.local_map.set_position(-36.852095, 174.763180)
        self.local_map.set_zoom(7)

        # button to show the markers
        self.show_markers_button = ctk.CTkButton(
            helpful_locations_frame,
            text="Show Markers",
            command=self.marker_button
        )
        self.show_markers_button.pack(padx=10, pady=5)

    def marker_button(self):
        """Show markers for helpful locations on the map.

        these markers are currently hardcoded for demonstration purposes.
        If I were to expand this, I would use an API to fetch real locations
        based on the user's location and desires.
        """
        premade_markers = [
            {"name": "Salvation Army Family Store", "lat": -36.8667, "lon": 174.7762},
            {"name": "SPCA Op Shop", "lat": -36.8700, "lon": 174.7830},
            {"name": "Auckland Council Recycling Centre", "lat": -36.9250, "lon": 174.7830},
            {"name": "Habitat for Humanity ReStore", "lat": -36.8850, "lon": 174.7750},
        ]
        for marker in premade_markers:
            self.local_map.set_marker(
                marker["lat"],
                marker["lon"],
                text=marker["name"]
            )

    def show_ai_next_steps(self):
        """Show the AI predicted next steps for the user's items.

        This function fetches the item list from the database and uses the list
        of items to get AI predictions. The predictions are displayed in the
        prediction_display textbox. The AI call is done in a separate thread to
        avoid blocking the UI, so the user sees a loading message while
        waiting, and they can still interact with the window, the map, etc.
        """
        print("Loading predictions...")
        self.prediction_loading_label.configure(
            text="Loading predictions, please wait..."
        )

        # Fetch item list on the main thread
        item_rows = functions.get_item_list(self.conn)
        item_names = [row[1] for row in item_rows]  # Extract names from the rows

        def load_predictions():
            # Now only do the AI call in the thread
            predictions = functions.ai_predicted_next_steps(item_names)
            def on_main_thread():
                self.prediction_loading_label.configure(text="")
                self.prediction_display.delete("1.0", "end")
                if not predictions:
                    self.prediction_display.insert(
                        "end",
                        "No predictions available.\n"
                    )
                else:
                    self.prediction_display.insert("end", predictions)
            self.root.after(0, on_main_thread)

        import threading
        threading.Thread(target=load_predictions).start()

    def _return_to_main(self):
        """Return to the main page.
        """
        self.root.destroy()
        from MainPage import MainPage
        MainPage(self.conn, self.username).run()

    def run(self):
        """Run the main loop for the Next Steps page.
        """
        self.root.mainloop()
