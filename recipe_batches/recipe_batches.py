#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Compare two dictionaries to each other
  # Compare the first dictionary's values (the recipe) to the second (ingredients)
  # Loop through it once to see if there's enough (subtract the recipe from the ingredients)
  # if so, loop again to see if there's enough remainding for other batches
  # if not, then stop looping and return the amount available
  
  total = 9999
  #Iterating through the dictionary
  for key, value in recipe.items():
    #Comparing to see if the ingredients exist
    if (len(recipe) != len(ingredients)):
          return 0
    if ingredients[key]:
      #If it exist then get the modulo of recipe in ingredients.
      temp = ingredients[key] / value
      #assign the modulo value to total, if the modulo value is less than total, replace it.
      if (temp < total):
        total = temp

    else:
      return 0
  return int(total)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))