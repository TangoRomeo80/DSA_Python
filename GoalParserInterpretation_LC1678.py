class Solution:
    def interpret(self, command: str) -> str:
        # return command.replace("()","o").replace("(al)","al")
        #Solution without built in functions
        # Create a map of the different interpretations
        interpretation_map = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
    
        # Split the command into a list of substrings
        substrings = re.findall(r"G|\(\)|\(al\)", command)
    
        # Initialize an empty result string
        result = ""
    
        # Iterate over the substrings and look up their interpretation in the map
        for substring in substrings:
            result += interpretation_map[substring]
    
        # Return the result
        return result