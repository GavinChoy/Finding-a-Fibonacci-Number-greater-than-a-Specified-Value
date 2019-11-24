#    Finding a Fibonacci Number greater than a Specified Value
#    Copyright (C) 2019 Gavin Choy
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

print("--------------------------------------------------------------------------------------------------")
print('')
print("    Finding a Fibonacci Number greater than a Specified Value")
print("    Copyright (C) 2019 Gavin Choy")
print("    This program comes with ABSOLUTELY NO WARRANTY; for details please see the LICENSE file.")
print("    This is free software, and you are welcome to redistribute it")
print("    under certain conditions; please see the LICENSE file for details.")
print('')
print("--------------------------------------------------------------------------------------------------")
print('')

# function to return a fibonacci number of a minimum size
def FibonacciGreaterThan(n):

    # initialise the first 2 numbers
    num1 = 1
    num2 = 1

    # loop until sufficiently large
    while num2 < n:

        # calculate the next number
        num3 = num1 + num2

        # set counters to new numbers
        num1 = num2
        num2 = num3

    #print result
    print(num2)


# main

# call function to return a fibonacci number with size of at least 10**1000
FibonacciGreaterThan(10**1000)
