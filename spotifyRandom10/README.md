**Project Title: Spotify Random 10**

**Author:** Osiro Asunde

**Description:**
The "Spotify Random 10" project is a web application that allows users to search for random music tracks based on a specified year using the Spotify API. The application presents a simple user interface where users can input a year, and upon submission, it retrieves and displays a list of up to 10 random music tracks released in that year. Users can listen to previews of the tracks directly on the website.

**Purpose:**
The project aims to provide users with a convenient way to discover and explore music from a specific year. By leveraging the Spotify API, users can quickly access a curated list of music tracks without needing to navigate through the Spotify app or website.

**Technologies and Libraries Used:**
- Python: Backend development using Flask framework.
- Flask: Micro web framework for building web applications.
- HTML/CSS: Frontend development for creating user interface and styling.
- Spotify API: Used to search for music tracks based on the specified year.
- Requests: Python library for making HTTP requests to the Spotify API.

**Challenges Faced:**
1. **Spotify API Authentication:** Implementing authentication with the Spotify API using OAuth 2.0 posed a challenge initially. However, by following the documentation and utilizing the `requests` library with proper authentication headers, the issue was resolved.
  
2. **Rendering Audio Previews:** Integrating audio previews of music tracks within the web application required understanding how to embed audio elements in HTML and dynamically render them based on the retrieved track information. Through experimentation and referencing online resources, this functionality was successfully implemented.

**Code Repository:**
The code for this project can be found in the GitHub repository at the following link: [Spotify Random 10](https://github.com/OsiroA/Python_projects/tree/main/spotifyRandom10)

**Additional Notes:**
Feel free to explore and contribute to the project by providing feedback or suggesting enhancements. Your contributions are highly appreciated!
