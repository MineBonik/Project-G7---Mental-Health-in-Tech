"""
Shared cleaning helpers

Used by every per-wave notebook (02a_clean_2014, 02b_clean_2016, ...), so all 
waves end up with the same labels: Gender, 3rd answer, etc.

In a notebook (notebooks/ is one level below src/):
    import sys; sys.path.append("../src")
    from cleaning import AGE_MIN, AGE_MAX, MALE, FEMALE, UNUSABLE, UNSURE_MAP, ORDER_WORK, ORDER_LEAVE, ORDER_EMP
"""

AGE_MIN, AGE_MAX = 14, 100

# ---------------------------------------------------------------- Gender
# Lower-cased and stripped before lookup. For a new wave, first print the values that
# are not in any set and decide where each one goes. In the 2016 notebook the OTHER set
# is defined there, and a value that is not listed raises an error.
MALE = {
    # 2014
    "male", "m", "make", "cis male", "man", "maile", "mal", "male (cis)",
    "msle", "mail", "malr", "cis man",
    "ostensibly male, unsure what that really means",
    # 2016
    "male.", "m|", "dude", "cisdude", "sex is male",
    "i'm a man why didn't you make this a drop down question. you should of asked sex? and i would of answered yes please. seriously how much text can this take?",
}
FEMALE = {
    # 2014
    "female", "f", "woman", "femake", "cis-female/femme", "female (cis)",
    "cis female", "femail",
    # 2016
    "i identify as female.", "female/woman", "cisgender female", "cis-woman",
    "fem", "female (props for making this a freeform field, though)",
    "afab", "female assigned at birth",
    # my choice: "afab" and "female assigned at birth" counted as female (2 answers). 2016 data
    # This is an assumption; the answers don't state current gender identity.   
}
UNUSABLE = {  # no usable answer -> NaN
    "a little about you", "p",
    # 2016
    "n/a", "none of your business", "human", "unicorn", "",
}

# ---------------------------------------------------------------- Unsure
UNSURE_MAP = {
    "Don't know": "Unsure", "I don't know": "Unsure",
    "Not sure": "Unsure", "I am not sure": "Unsure", "I'm not sure": "Unsure",
    "Maybe": "Unsure", "Maybe/Not sure": "Unsure",
}


# -------------------------------------------------------------- Ordering
ORDER_WORK = ["Never", "Rarely", "Sometimes", "Often"]
ORDER_LEAVE = ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult"]
ORDER_EMP = ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"]
