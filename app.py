from flask import Flask, render_template, jsonify

app = Flask(__name__)
names = {
    "first_name": "Christopher", 
    "last_name": "Liu"
}
contact = {
    "phone": "614-440-9393",
    "email": "chrisliu317@gmail.com"
}
skills = {
    "languages": {
        "python": "for back-end development",
        "javascript": "for front-end development",
        "typescript": "for javascript that works",
        "html": "for creating pages",
        "css": "for styling pages",
        "scss": "for an easy and sassy css",
        "go": "for when you gotta go fast",
        "java": "for academic masochism",
        "csharp": "for fun and games"
    },
    "frameworks":["Django", "Flask"],
    "databases":["postgreSQL", "SQLite"],
    "version_control": "Git",
    "deployment": "Docker",
}
projects = {
    "Course Helper":["django framework, orm, rest api, ajax", "python, typescript, scss, html"],
    "Sorting Visualisation": ["algorithms", "javascript, css"],
    "Chess, Tetris, Snake, Tank Games": ["oop, gui", "python, java, oojs"],
}
experience = {
    "Part time - Crew Member": ["Chipotle", "high school summer job"],
}
education = {
    "High school": ["Upper Arlington", "Class of 2020"],
    "College": ["The Ohio State Univeristy",]
}

@app.route('/')
def resume():
    return render_template("extras.html", 
            namedata=names.items(), 
            contactdata=contact.items(),
            skillsdata=skills.items(),
            projectsdata=projects.items(),
            experiencedata=experience.items(),
            educationdata=education.items(),
            )

@app.route('/api')
def resumeapi():
    return jsonify({
        "first_name":names.get("first_name"),
        "last_name":names.get("last_name"),
        "contact":contact,
        "skills":skills,
        "projects":projects,
        "experience":experience,
        "education":education,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)


