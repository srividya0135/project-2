import re#importing regular expression library

#word_count function
def count_words(text):
    """
    This function counts the number of words in the input text.
    Commas, hyphens, full stops, and newlines are used as separators.
    :param text: str, the input text (single or multiple paragraphs)
    :return: int, the number of words in the text
    """
    # Remove newline characters
    text = text.replace('\n', ' ')
    # Use regex to split the text by spaces, commas, hyphens, and full stops
    words = re.findall(r'\b\w+\b',text)
    # Remove any empty strings from the list
    words = [word for word in words if word]#list comprehension
    return len(words)

def main():
    """
    This function handles user input and displays the word count.
    """
    while True:
        try:
            # this print statement help us like a friendly interface by providing a meaning full prompt
            print("Enter your text (on completion of entering text Enter EXIT on next line):")
            user_input = []
            while True:
                line = input()
                if line.lower() == 'exit':
                    break
                user_input.append(line)
            
            user_input = ' '.join(user_input).strip()
            
            # Check for empty input
            if not user_input:
                raise ValueError("Input cannot be empty. Please enter valid text.")
            
            # Count the words and display the result
            word_count = count_words(user_input)
            print(f"Word count: {word_count}")

            #ask the user if they want to enter another input and read the answer(yes/no)
            #note:if the user enter NO , no , No ,nO ===>it is considered as no
            #in all other cases if consider your answer is YES.
            next=input("Do You Want To Give Another Input(yes/no):").strip().lower()
            if next=='no':
                print("Thanks For Trusting Us!!\nHave A Nice Day!!!")
                break
            
        
        except ValueError as e:
            print(e)

# Run the main function

main()
