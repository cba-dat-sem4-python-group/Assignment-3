# Assignment 3: numpy
This assignment is about slicing and .

## How to hand in
The assignment is expected to be published on GitHub, but the actual hand-in is on peergrade and should contain only a link to a MyBinder. Remember her to use the link provided when first registering your notebook with mybinder (not the url taken from your browsers adress field). See the notebook 12-Assignments for more information.

## Create jupyter notebook with 4 data illustrations
1. First create a file with your python module. This is where you should put your functions to be used in the notebook.
2. Second create a function to read the csv file containing Copenhagen city population data and return a numpy array (numpy.ndarray). hint: use np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1) as in the slides
3. Third create a function that can extract the number of all the citizens from native english speaking countries and from non english speaking countries. How many are there of each? (hint remember that with python you can return multiple values from a function).
4. Now create another function that can take 2 arguments:
    - 1: the dataset in the form of a 2dimensional data array where y=data rows and x=[year, area, age nationality, amount].
    - 2: the mask in the form: data[:,3] == 5120 to find swedish or data[:,0] == 1999 to filter on year
the return value must be the filtered dataset.
5. Create another function that can take 2 arguments:
    - a dataset with same characteristics as above and
    - a value for the x-axis (either year, area, age or nationality)
    - return value should be the accumulated population for all x-values.
    - hint: if year is chosen for x then y is all accumulated amounts from all areas, ages and nationalities.
6. Create Illustration 1: In your notebook use the above function and create a 2d array of year as x and accumulated amount as y:
create a line graph of the population change over time for all of Copenhagen
7. Create illustration 2: In your notebook use your module to create a dataset where development of all German citizens can be shown over time
8. Create illustration 3: Show a bar plot of all the 18-25 year old in the different areas of copenhagen and in the same plot show (in a different color) all 60-67 year old in the different areas.
9. Create illustration 4: show a pie chart of age groups (0-10, 10-20, 20-30 ...) in Østerbro part of Copenhagen. create another similar piechart for Vesterbro.
