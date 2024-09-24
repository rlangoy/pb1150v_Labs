class Subject:
    """A class that maintains a list of observers and notifies them of changes."""

    def __init__(self):
        """Initializes a new Subject instance with an empty list of observers."""
        self.observerCollections = []

    def registerObserver(self, observer):
        """Registers an observer to be notified of changes.

        Args:
            observer (Observer): The observer instance to be registered.
        """
        self.observerCollections.append(observer)

    def unregisterObserver(self, observer):
        """Unregisters an observer so it will no longer receive notifications.

        Args:
            observer (Observer): The observer instance to be unregistered.
        """
        self.observerCollections.remove(observer)

    def notifyObservers(self, message):
        """Notifies all registered observers with the provided message.

        Args:
            message (str): The message to send to all observers.
        """
        for observer in self.observerCollections:
            observer.update(message)


class Observer:
    """An abstract base class for observers that want to receive updates from a Subject."""

    def update(self, message):
        """Updates the observer with a new message.

        Args:
            message (str): The message from the Subject.
        """
        pass


class ConcreteObserverA(Observer):
    """A concrete implementation of the Observer that prints received messages."""

    def update(self, message):
        """Prints the message received from the Subject.

        Args:
            message (str): The message from the Subject.
        """
        print(f"ObserverA received message: {message}")


class ConcreteObserverB(Observer):
    """A concrete implementation of the Observer that prints received messages."""

    def update(self, message):
        """Prints the message received from the Subject.

        Args:
            message (str): The message from the Subject.
        """
        print(f"ObserverB received message: {message}")


# Example usage
if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserverA()
    observer2 = ConcreteObserverB()

    subject.registerObserver(observer1)
    subject.registerObserver(observer2)

    subject.notifyObservers("State changed!")  # Both observers receive the message.
