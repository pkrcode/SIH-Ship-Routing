
# SIH Ship Routing

This project is part of the **Smart India Hackathon (SIH) 2024**, where the goal is to develop a ship routing optimization system. The system uses an advanced A* pathfinding algorithm for efficient navigation, considering factors like wind, ocean currents, fuel efficiency, and various heuristics like cargo, passenger comfort, and speed.

## Features

- **Pathfinding**: Utilizes the A* algorithm to find the optimal path for ship navigation.
- **Environmental Alignment**: Takes into account wind and ocean current data to optimize routing.
- **Fuel Efficiency**: Incorporates fuel cost as a factor for the route optimization.
- **Heuristics**: Multiple heuristics for cargo, passenger, and fuel efficiency-based optimization.
- **Real-Time Data**: Integrates real-time weather and environmental data for dynamic pathfinding.
- **Interactive UI**: Built using Pygame to visualize paths and interactively select start and end points.

## Project Setup

### Prerequisites

- Python 3.x
- Pygame
- TensorFlow (if needed for any AI-related tasks)
- MySQL (for database management)
- Firebase (for remote monitoring)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pkrcode/SIH-Ship-Routing.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup the environment variables (if required). Create a `.env` file based on `.env.example` and fill in the necessary values.

### Running the Project

To run the project, execute the following command:

```bash
python ActualMain.py
```

This will start the ship routing optimization system with real-time data visualization.

### Testing

You can test the system with sample data provided in the `combined_2024-08-29.csv` (and other similar files). Ensure that the weather and environmental data is up to date for accurate pathfinding results.

## Contribution

Feel free to fork this repository and submit pull requests. Contributions to improve the algorithm, add new features, or fix bugs are welcome.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is for **internal use only** by the development team participating in the **Smart India Hackathon (SIH) 2024**. Redistribution, modification, or public use outside of this team is prohibited without the written consent of the team members.

All rights reserved by the contributors.

## Acknowledgments

- Special thanks to the SIH organizers and mentors for their support.
- Thanks to all the contributors who have helped improve the project.
