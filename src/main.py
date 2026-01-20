#!/usr/bin/env python3
"""
Password Generator

A small CLI tool to generate secure passwords while practicing:
- input validation
- clean function design
- defensive programming
"""

from __future__ import annotations

import secrets
import string


def read_int(prompt: str, min_value: int, max_value: int) -> int:
    """Read an integer within a given range."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer from the user."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def build_alphabet(use_lower: bool, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    """Build the character set based on selected options."""
    alphabet = ""
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        # Common, generally accepted symbols. Avoid spaces.
        alphabet += "!@#$%^&*()-_=+[]{};:,.?/"
    return alphabet


def generate_password(length: int, alphabet: str) -> str:
    """Generate a password using cryptographica
