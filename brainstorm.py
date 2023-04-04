import openai
#import argparse
import webbrowser

data_dir = "<<Your Path to the data directory>>"

#p = argparse.ArgumentParser(description='Brainstorm idea')

#p.add_argument('--idea', type=str, required=True, help='Idea suggestions')

#args = p.parse_args()

def open_file(file_name):
    with open(data_dir + file_name, 'r') as f:
        return f.read()
    
def write_file(file_name, text):
    with open(data_dir + file_name, 'w') as f:
        f.write(text)
        return

#open html file in default browser
def open_html(file_name):
    with open(data_dir + file_name, 'r') as f:
        ideas_html = f.read()
    return ideas_html


openai.api_key = open_file('api_key.txt')

sys_prompt = open_file('prompt.txt')

assistant_reply_best = open_file('assistant_reply_best.txt')

def brainstorm_html_idea_and_write(idea):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #model="gpt-4",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": "brainstorm --idea ai --output HTML"},
            {"role": "assistant", "content": assistant_reply_best},
            {"role": "user", "content": f"brainstorm --idea {idea} --output HTML"}
        ]
    )
    #print(output.choices[0].message.content)
    write_file(f'{idea}.html', output.choices[0].message.content)
    return output.choices[0].message.content


#def main(idea):
    #return brainstorm_html_idea_and_write(idea)

#if __name__ == '__main__':
    #brainstorm_html_idea_and_write(args.idea)
    #open_html(f'{args.idea}.html')
    #main(args.idea)
