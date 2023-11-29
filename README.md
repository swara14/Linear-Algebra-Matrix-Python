<h1>Linear-Algebra-Matrix-Python</h1> 

<h2>Overview:</h2>
This project is a Python script that reads a matrix from a file, transforms it to <b>Reduced Row Echelon Form (RREF)</b>, and provides the parametric solution for the system of linear equations. The script utilizes <b>Python 3</b> and the <b>Sympy library</b> for symbolic mathematics.

<h2>Language and Library:</h2>
Language: Python 3.x

Library: Sympy

<h2>Implementation:</h2>

1. Reading the Matrix
The script reads a matrix from the file maths.txt, where each row is newline-separated, and elements in each row are space-separated. The matrix elements are converted to floating-point numbers.

2. Reduced Row Echelon Form (RREF)
The matrix is sorted in reverse order, and the Sympy library is employed to obtain the RREF and identify pivot indices.

4. Parametric Form
The RREF matrix is transformed into parametric form, with columns extracted for further calculations.

5. Identifying Pivot and Non-Pivot Columns
Pivot and non-pivot columns are identified for subsequent solution generation.

6. Generating the Solution
The script creates the parametric solution for the system of linear equations.

7. Rounding Off
To enhance readability, rounding off is performed for cleaner output.

8. Displaying the Solution
The final solution is displayed, presenting the system of linear equations in parametric form.

<h3>Assumptions:</h3>
Ensure that the matrix is correctly formatted in maths.txt.

Run the script using Python 3.
