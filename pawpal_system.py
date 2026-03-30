from dataclasses import dataclass


@dataclass
class Pet:
    """Pet class representing a pet in the PawPal system."""
    name: str
    species: str
    age: int
    weight: float
    health: str
    
    def updateinfo(self):
        """Update pet information."""
        pass
    
    def viewdetails(self):
        """View pet details."""
        pass
    
    def updatehealth(self):
        """Update pet health status."""
        pass


@dataclass
class Task:
    """Task class for pet-related tasks."""
    pass
