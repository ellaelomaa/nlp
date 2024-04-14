
from threading import Thread
from time import sleep
from queue import Queue
from enum import Enum, auto
from tkinter import ttk

class TicketPurpose(Enum):
    UPDATE_PROGRESS_TEXT = auto()
    # NLP:hen: tehdyt/yhteensä, teksti missä mennään

class Ticket:
    def __init__(self,
                 ticket_type: TicketPurpose,
                 ticket_value: str):
        self.ticket_type = ticket_type
        self.ticket_value =ticket_value

class MainWindow(ttk.Tk): # Super class
    def __init__(self):
        super().__init__() #super() wakes up tk.Tk

        self.geometry("640x480")

        self.queue_message = Queue()

        self.create_frame_buttons().pack(expand=True)

        self.bind("<<CheckQueue>>", self.check_queue)
    
    def check_queue(self, event): # In the main thread
        """
        Read the queue
        """
        msg: Ticket # Type hint
        msg = self.queue_message.get()

        if msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_TEXT:
            self.lbl_status.configure(text=msg.ticket_value)

    def create_frame_buttons(self) -> ttk.Frame:
        """
        Create and return a frame that contains buttons
        """

        self.frame_buttons = ttk.Frame(self)
        
        self.btn_download = ttk.Button(self.frame_buttons, 
                                       text="Download",
                                       command=self.on_download_button_clicked)

        self.btn_test = ttk.Button(self.frame_buttons,
                                   text="Test",
                                   command=self.on_test_button_clicked)
        
        self.lbl_status = ttk.Label(self.frame_buttons)
        
        self.btn_download.pack()
        self.btn_test.pack()
        self.lbl_status.pack()

        return self.frame_buttons
    
    def on_test_button_clicked(self):
        print("Test")

    def on_download_button_clicked(self):
        new_thread = Thread(target=self.download, 
                            args=("sky.jpg", ),
                            daemon=True # When main thread exits, this thread will too
                            )
        new_thread.start()
    
    def download(self, file_name: str):
        """
        Download in a separate thread
        """
        for progress in range(1, 101): # goes up to 100 (%)
            ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                            ticket_value=f"Downloading {file_name}...{progress} %")
            self.queue_message.put(ticket)
            self.event_generate("<<CheckQueue>>") # virtual event with an arbitary name
            sleep(1)
        
        ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                        ticket_value="Finished downloading!")
        self.queue_message.put(ticket)
        self.event_generate("<<CheckQueue>>")

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()