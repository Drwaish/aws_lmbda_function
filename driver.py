""" driver function of aws lambda"""
import json
from lambda_function import lambda_handler


def prompt_generate(paragraph : str)-> str:
    '''
    Create prompt pass to lambda function.

    Parameters
    ----------
    paragraph
        paragraph to detect Noun

    Return
    ------
    str
    '''
    prompt = f'''
        "Noun is the name of person,place, ideas and things". \
        Consider above definition, identify nouns from text \
        given in triple double quotes and return \
        in python's list.\
        """{paragraph}"""
        ''' 
    return prompt

def main():
    '''
    Request for lambda function.

    Parameters
    ----------
    None

    Return
    ------
    None
    '''
    text = """
            Martin Luther King Jr. led many demonstrations against racism.\
            He delivered his message in a non-violent manner. \
            Some members of his movement later engaged in less peaceful
            protests. Luther King was detained several times. 
            The longest jail sentence he received was four months.
            """
    prompt = prompt_generate(text)
    request =  {
                "prompt" : prompt,
                "isBase64Encoded": False
                }

    content = None
    requests = {}
    requests["body"] = json.dumps(request)
    response =lambda_handler(requests, content)
    print(response['body'])

if __name__ == "__main__":
    main()
