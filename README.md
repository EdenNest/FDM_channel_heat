
# Heat Transfer Simulation Using Finite Difference Method (FDM)

## Overview
This project implements the Finite Difference Method (FDM) to numerically solve a steady-state heat conduction problem in a specified domain. The simulation calculates temperature distribution within a square channel subjected to different boundary conditions, using Python.

## Project Structure
- `heattransfer.py`: The main Python script for performing the heat transfer simulation.
- `heat transfer.pdf`: Contains the project report and detailed documentation of the problem setup, methodology, and results.

## Getting Started
To run this project, follow these steps:

### Prerequisites
- Python 3.x installed on your machine.
- Python libraries: numpy and matplotlib. Install them using:
  ```bash
  pip install numpy matplotlib
  ```

### Running the Simulation
1. **Open Command Prompt** and navigate to the project directory.
2. **Run the script** by typing:
   ```bash
   python heattransfer.py
   ```
3. Follow the on-screen prompts to input the values of `delta x` and `T inside` when asked by the script.

## Inputs
- `delta x`: The grid spacing in the x-direction. Valid inputs are `0.005` or `0.01`.
- `T inside`: The internal surface temperature. Valid inputs are `500`, `600`, or `700` degrees Kelvin.

## Outputs
- Temperature distribution across the mesh.
- Heat loss calculations and comparisons using different boundary conditions.
- Visualizations of the temperature field in 3D.

## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

