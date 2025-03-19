# CODE World Campus

A silly little text adventure. 

## Adding a location

Locations are organized in files. Each location is its own file. 

You can add a location by following these steps: 

1. Add a file in the **/locations** directory. 
2. The file must include a variable defining a dictionary. That dictionary must follow the following structure: 

```python
location_variable = {
  "USER_INPUT": {
    "output": function_name,
    "next_location_id": None
  }
}
```

Replace the `location_variable` with a unique name. 

For each possible user input, add a dictionary. The dictionary must have a `output` and `next_location_id` value. 

The `output` should be assigned a function and `return` a string to display to the user. 

The `next_location_id` should be any ID available in the `locations` dictionary in the **main.py** file if the user in put should change the location to that place. Use `None` if the location should not be changed.

Define a `"fallback"` as `USER_INPUT` for one of the dictionaries to catch all not-matched user inputs. 

Once the room is defined: 

1. Import the room's dictionary variable in the **main.py** file. 
2. Give the location an ID and define it as _key_ in the `locations` variable of the **main.py** file. Reference the imported room to that key (see other rooms as example).
3. Ensure your room is accessible from anywhere in the existing game by adding its ID string (defined above) as `next_location_id` to another room. 