# Phone_Numbers
Collaboration between Aggrey and Dante

Phone Number Processor

A Python program that reads, validates, normalizes, and sorts North American phone numbers using a custom PhoneNumber class.

Overview

Handles multiple phone number formats

Converts letters to digits (e.g., 1-800-POTATO-3)

Validates numbers using NANP rules

Stores area_code, exchange_code, and line_number

Supports comparison, printing, and integer conversion

Reads a file of names and numbers, returning a sorted list

Features

PhoneNumber Class

Accepts strings or integers

Removes extra symbols

Validates NANP rules

Implements int(), str(), repr(), and < operator

read_numbers() Function

Reads a UTF-8 file

Extracts names and phone numbers

Returns a sorted list of valid (name, PhoneNumber) tuples
