#Installing Dependencies 

Before Installing the dependencies, create a virtual environment. 

I created a virtual environment using the command below (I had various versions of python running on my host compute)

$ python3 -m venv env 

Then I activated the environemnt by running 

$ source env/bin/activate 

The command for activating the virtual environment is specific to my Mac Environment.

After the activation, I downloaded the packages I needed for analytics using:

python3 -m pip install pandas numpy matplotlib 

