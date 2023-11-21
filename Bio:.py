class Bio:
    def __init__(self, name, role, location, interests, skills):
        self.name = name
        self.role = role
        self.location = location
        self.interests = interests
        self.skills = skills

    def display_bio(self):
        bio = (
            f"👋 Hi, I'm {self.name}.\n"
            f"🌍 Based in {self.location}.\n"
            f"👨‍💻 {self.role} with a passion for {', '.join(self.interests)}.\n"
            f"💡 Skills: {', '.join(self.skills)}.\n"
            "🚀 Let's collaborate and build amazing things together!\n "
            "I have a deep interest in and am passionate about data and machine learning."
        )
        return bio

my_bio = Bio(
    name="Raz Adibah",
    role="Junior Data Analyst",
    location="Johor Bahru, Malaysia",
    interests=["coding", "open source", "machine learning"],
    skills=["Python", "SQL", "PowerBI", "Bash", "R"]
)

# Display the bio
print(my_bio.display_bio())