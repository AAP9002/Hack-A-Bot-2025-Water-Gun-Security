from numpy import add
import cv2

class Sentry():
    def add_system_name(self, frame, name):
        """add the device name in the top left corner with an active status

        Args:
            name (str): the text to add
        """
        cv2.putText(frame,
                    name,  # Text to display
                    (10, 30),  # Position where the text will be drawn
                    cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                    1,  # Font size
                    (255, 0, 0),  # Text color in BGR (red in this case)
                    2)
        


    def process_frame(self, frame):
        # This method should be overridden in subclasses
        self.add_system_name(frame, "Sentry System: Active")
    
    def classify_mood(self, frame):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")
    
    def find_face(self, frame):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")
    
    def add_text(self, frame, text):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")
    
    def notify_system(self, message):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")