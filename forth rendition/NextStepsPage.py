import customtkinter as ctk
import functions
import tkintermapview
import time
import random
ctk.set_default_color_theme("forth rendition/theme.json")

class NextStepsPage:
    def __init__(self, conn, username):
        self.conn = conn
        self.username = username

        # use CTk window instead of Tk
        self.root = ctk.CTk()
        self.root.title("Next Steps")
        self.root.resizable(True, True)
        self.prediction_display = None
        self.local_map = None

        self._create_widgets()

    def _create_widgets(self):
        # =========== Frames ===========
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill="x")

        body_frame = ctk.CTkFrame(self.root)
        body_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # mimic “LabelFrame” by adding a label on top
        next_steps_label = ctk.CTkLabel(body_frame, text="Predicted Actions", font=("Arial", 15))
        next_steps_label.pack(anchor="w", padx=10)
        next_steps_frame = ctk.CTkFrame(body_frame)
        next_steps_frame.pack(padx=10, pady=(0, 10), fill="x")

        helpful_locations_label = ctk.CTkLabel(body_frame, text="Helpful Locations", font=("Arial", 15))
        helpful_locations_label.pack(anchor="w", padx=10)
        helpful_locations_frame = ctk.CTkFrame(body_frame)
        helpful_locations_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        # =========== Title Area ===========
        ctk.CTkButton(title_frame, text="← Back to Main Page", command=self._return_to_main).pack(
            side="left", padx=10, pady=5
        )

        ctk.CTkLabel(
            title_frame, text="Like A Knife Through Clutter", font=("Papyrus", 24)
        ).pack(side="right", padx=10, pady=5)

        ctk.CTkLabel(
            title_frame, text=f"{self.username}'s Next Steps!", font=("Arial", 15)
        ).pack(anchor="center", padx=5, pady=5)

        # =========== Predicted Steps Area ===========
        ctk.CTkLabel(
            next_steps_frame,
            text="Here you can find the predicted next steps for what you should do with your items!",
            wraplength=600,
        ).pack(anchor="center", padx=5, pady=5)

        ctk.CTkButton(next_steps_frame, text="Get Next Steps", command=self.show_ai_next_steps).pack(
            padx=10, pady=5
        )

        # Textbox for predictions
        self.prediction_display = ctk.CTkTextbox(next_steps_frame, height=200, width=600, wrap="word")
        self.prediction_display.pack(padx=10, pady=5)

        # placeholder for the loading label
        self.prediction_loading_label = ctk.CTkLabel(next_steps_frame, text="")
        self.prediction_loading_label.pack(padx=10, pady=5)

        # =========== Map Area ===========
        ctk.CTkLabel(helpful_locations_frame, text="Helpful Locations Near You:").pack(
            anchor="center", padx=5, pady=5
        )

        # the map
        self.local_map = tkintermapview.TkinterMapView(
            helpful_locations_frame, width=helpful_locations_frame.winfo_width(), height=200, corner_radius=0
        )
        self.local_map.pack(padx=10, pady=10, fill="x", expand=True)
        self.local_map.set_position(-36.852095, 174.763180)
        self.local_map.set_zoom(7)

        # button to show the markers
        self.show_markers_button = ctk.CTkButton(
            helpful_locations_frame, text="Show Markers", command=self.marker_button
        )
        self.show_markers_button.pack(padx=10, pady=5)

    def marker_button(self):
        # Hardcoded locations (replace/add as needed)
        premade_markers = [
            {"name": "Salvation Army Family Store", "lat": -36.8667, "lon": 174.7762},
            {"name": "SPCA Op Shop", "lat": -36.8700, "lon": 174.7830},
            {"name": "Auckland Council Recycling Centre", "lat": -36.9250, "lon": 174.7830},
            {"name": "Habitat for Humanity ReStore", "lat": -36.8850, "lon": 174.7750},
        ]
        for marker in premade_markers:
            self.local_map.set_marker(marker["lat"], marker["lon"], text=marker["name"])

    """   
    def marker_button(self):
        def add_markers():
            suitable_places = [
                'donation bins', 'op shops', 'salvation army', 'red cross', 'SPCA op shop',
                'thrift store', 'habitat for humanity', 'city mission',
                'landfill', 'council waste disposal', 'recycling center',
                'charity shop'
            ]
            for place in suitable_places:
                results = functions.search_nearby_places(place, -36.852095, 174.763180)
                print(results)
                for r in results:
                    print(r)
                    self.root.after(0, lambda r=r: self.local_map.set_marker(r['lat'], r['lon'], text=r['name']))
                    self.root.update()
        import threading
        threading.Thread(target=add_markers).start()
        """


    def show_ai_next_steps(self):
        print("Loading predictions...")
        self.prediction_loading_label.configure(text="Loading predictions, please wait...")

        # Fetch item list on the main thread
        item_list = functions.get_item_list(self.conn)

        def load_predictions():
            # Now only do the AI call in the thread
            predictions = functions.ai_predicted_next_steps(item_list)
            def on_main_thread():
                self.prediction_loading_label.configure(text="")
                self.prediction_display.delete("1.0", "end")
                if not predictions:
                    self.prediction_display.insert("end", "No predictions available.\n")
                else:
                    self.prediction_display.insert("end", predictions)
            self.root.after(0, on_main_thread)

        import threading
        threading.Thread(target=load_predictions).start()

    def _return_to_main(self):
        self.root.destroy()
        from MainPage import MainPage
        MainPage(self.conn, self.username).run()

    def run(self):
        self.root.mainloop()
