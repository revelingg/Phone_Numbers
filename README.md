# Phone_Numbers (Collaboration between Aggrey and Ibukun)

**Phone Number Processor**

  A Python program that reads, validates, normalizes, and sorts North American phone numbers using a custom PhoneNumber class.

**Overview**

  1. Handles multiple phone number formats
  2. Converts letters to digits (e.g., 1-800-POTATO-3)
  3. Validates numbers using NANP rules
  4. Stores area_code, exchange_code, and line_number
  5. Supports comparison, printing, and integer conversion
  6. Reads a file of names and numbers, returning a sorted list

**Features**

  1. PhoneNumber Class
  2. Accepts strings or integers
  3. Removes extra symbols
  4. Validates NANP rules
  5. Implements int(), str(), repr(), and < operator
  6. read_numbers() Function
  7. Reads a UTF-8 file
  8. Extracts names and phone numbers
  9. Returns a sorted list of valid (name, PhoneNumber(number) tuples
