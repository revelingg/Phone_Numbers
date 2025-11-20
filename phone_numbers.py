
# Ibukun Adenuga
# Aggrey Narh
from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}



def read_numbers(path):
    
    """ 
        Reads in the numbers and returns if following NAMP rules
       
        Args: Takes in the path of the string
        Returns: returns the list of objects
        Side Effects: Raises value error when needed
    """
    #namp numbers can have +,-, * and other seperatores
    namp_pattern = r"""
        ^(\+?1)?
        \D*
        (\d{3})
        \D*
        (\d{3})
        \D*
        (\d{4})
        $   #must end with 4 digits, optionally +1 start with, any character that isnt a number for delimeters then 3,3,4
        """
        
    with open(path, "r", encoding="utf-8") as file:  #opens the file and reads it
        
        valid_obj = [
            (name, PhoneNumber(number))
            for line in file
            for name,number in [line.strip().split("\t")]
            if re.fullmatch(namp_pattern,number, re.VERBOSE)
        ]    #list comprehension to create the objects if they match the pattern
        if not valid_obj:
            raise ValueError("No valid numbers found")
        valid_obj = sorted(valid_obj, key=lambda x: x[1]) 
        
        return valid_obj
        
    
                
            
            

class PhoneNumber():
    """
        Phone number class used to map numbers to the user
        
        Attributes:
            area_code: the area code of the number (str)
            exchange_code : the exhange code of the number (str)
            line_number: the line number (str)
            number(str): the full number
    """

    def __init__(self, number):
        """
            The init method for the phonenumber
            Args:
                number: this will the (str) or (int) that contains the number to be processed
            Raises:
                TypeError: when the number is not a string or integer
            Side Effects:
                Sets the values of the object
            
                
        """
       
        
        
        if not isinstance(number, (int,str)):
            raise TypeError("Not an integer or string value")
        else:
            number = str(number)
            self.number,self.area_code,self.exchange_code,self.line_number = self.validate(number) #sets values
            
    
    def validate(self,number):
        
        """
            Validates the string to make sure its a proper phone number
            Args: 
                number(string): Takes in the number
            Side Effects: 
                Raises value error when needed
            Returns: 
                returns the valid strings
        """
        
        #cleans the number converts the letters to numbrs and removes any characters 
        temp_num = re.sub(
            r"[^A-Za-z0-9]", #removes all that isnt a number/letter replaces it with "" from the result of the inner sub which is the converted letters
            "",
            
            re.sub(
                r"[A-Za-z]",
                lambda x: LETTER_TO_NUMBER.get(x.group().upper(),x.group()),
                number)
            
            ) 
        
        if temp_num.startswith("1") and len(temp_num) == 11:
           temp_num = temp_num[1:] #removes the country code if its there 
        
        
        reg_pattern = r"""

            ([2-9](?!11)\d{2})  #first digit must be 2-9 and not end with 11 moves to the next section
            ([2-9](?!11)\d{2}) #first digit must be 2-9 and not end with 11 moves next section
            (\d{4})$ #must end with 4 digits total makes 10 
            
            """
        
        match = re.fullmatch(reg_pattern, temp_num, re.VERBOSE)
        
        #if it doesnt match the rules of 10 characters, invalid number else continue
        if not match:
            raise ValueError("Invalid number")
        
        #stores the values from the groups 
        area = match.group(1)
        code = match.group(2)
        line = match.group(3)
        
        
        
        return temp_num, area,code,line
    
    def __repr__(self):
        """Formal representation of the string
            Returns: the formal representation of a string 
            
        """
        return f"PhoneNumber({self.number!r})"
    
    def __str__(self):
        """
            Information representation of the string
            Returns: the informal string
        """
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}" 
        
    def __lt__(self,other):
        """
            Magic Method that compares the numbers to see which is less, used in conjunction with the sort
            
            Returns: 
                returns the lesser number
        """
        return self.number < other.number
    
    def __int__(self):
        """Convers the object to an integer
            Returns: returns the int object
        """
        return int(self.number)



def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{name}\t{repr(number)}")  #remove the repr if u want the str representation
        
    #test cases delete after 
    n1 = PhoneNumber("1-800-POTATO-3")
    
    print(n1.area_code)
    print(n1.line_number) 
    print(n1)
    print(repr(n1))
    print(n1.number)


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
