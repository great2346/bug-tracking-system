import datetime

class BugTracker:
    """A simple console-based bug tracking system."""
    def __init__(self):
        self.bugs = []
        self.bug_id_counter = 1

    def add_bug(self, title, description):
        """Adds a new bug to the system."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_bug = {
            'id': self.bug_id_counter,
            'title': title,
            'description': description,
            'status': 'Open',
            'created': timestamp
        }
        self.bugs.append(new_bug)
        print(f"Bug {self.bug_id_counter} added successfully.")
        self.bug_id_counter += 1

    def list_bugs(self):
        """Lists all recorded bugs."""
        if not self.bugs:
            print("No bugs found.")
            return

        print("\n--- Current Bugs ---")
        for bug in self.bugs:
            print(f"ID: {bug['id']}, Title: {bug['title']}, Status: {bug['status']}, Created: {bug['created']}")
        print("--------------------")

    def update_bug_status(self, bug_id, new_status):
        """Updates the status of a specific bug."""
        for bug in self.bugs:
            if bug['id'] == bug_id:
                bug['status'] = new_status
                print(f"Bug {bug_id} status updated to '{new_status}'.")
                return
        print(f"Bug {bug_id} not found.")

    def run(self):
        """Main loop for the bug tracker console interface."""
        while True:
            print("\nBug Tracking System Menu:")
            print("1. Add a new bug")
            print("2. List all bugs")
            print("3. Update bug status")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                title = input("Enter bug title: ")
                description = input("Enter bug description: ")
                self.add_bug(title, description)
            elif choice == '2':
                self.list_bugs()
            elif choice == '3':
                try:
                    bug_id = int(input("Enter bug ID to update: "))
                    new_status = input("Enter new status (e.g., 'In Progress', 'Closed'): ")
                    self.update_bug_status(bug_id, new_status)
                except ValueError:
                    print("Invalid input. Please enter a number for the bug ID.")
            elif choice == '4':
                print("Exiting Bug Tracking System.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    tracker = BugTracker()
    tracker.run()
