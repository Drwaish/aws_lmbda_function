import json
import openai

def lambda_handler(event_jsonified, context):
    """
    lambda function to perform function.

    Parameters
    ----------
    event_jsonified
        Contain request header
    context
        Context of a function 

    Return 
    Dictionary Object

    """
    try:
        event = event_jsonified['body']
        event = json.loads(event, strict = False)
        prompt = event["prompt"]
        if prompt is not None:
            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
            model= "gpt-3.5-turbo",
            messages=messages,
            temperature=0, 
            )
            return (
                {
                'status_code' : 200,
                'headers': {'Content-Type': 'application/json'},
                'body': response.choices[0].message["content"],
                "isBase64Encoded": False
                }
            )
        else: 
            return {'statusCode': 404,
                         'Error' : "Bad Params", 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message': 'Text Not Available'  
                    }   
    except openai.error.Timeout as eror:
        return {'statusCode': 401,
                         'Error' : eror, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message':  "Retry your request after a brief wait and contact to OpenAI if the issue persists."
                    }
    except openai.error.APIError as eror:
        return {'statusCode': 401,
                         'Error' : eror, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message':  "Retry your request after a brief wait and contact to OpenAI if the issue persists."
                    }
    except openai.error.APIConnectionError as eror:
      #Handle connection error, e.g. check network or log
        return {'statusCode': 401,
                         'Error' : eror, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message':  "Retry your request after a brief wait and contact to OpenAI if the issue persists."
                    }
    except openai.error.InvalidRequestError as eror:
      #Handle invalid request error, e.g. validate parameters or log
        return {'statusCode': 400,
                         'Error' : eror, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message':"The error message should advise you on the specific error made.\
                                   Check the documentation for the specific API method you are calling and make sure you are sending valid and complete parameters. You may also need to check the encoding, \
                                   format, or size of your request data." 
                    }    
            
    except openai.error.AuthenticationError as eror:
      #Handle authentication error, e.g. check credentials or log
        return {'statusCode': 401,
                         'Error' : eror, 
                         'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                        'Message': 'Ensure the correct API key and requesting organization are being used.'   
                    }
    except openai.error.PermissionError as eror:
      #Handle permission error, e.g. check scope or log
        return {'statusCode': 403,
                    'Error' : eror, 
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*'
                    },
                    'Message': "Make sure your API key has the appropriate permissions for the action or model accessed."
                }
    except openai.error.RateLimitError as eror:
        return {'statusCode': 429,
                    'Error' : eror, 
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*'
                    },
                    'Message': 'Pace your requests. Read the Rate limit guide.'
                } 
    except openai.error.server_error as eror:
        return {
            'statusCode': 500,
                    'Error' : eror, 
                    'headers': {
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'Message': 'Internal Server Error'
                }
    except openai.error.tokens_exceeded_error as eror:
        return {
                'statusCode': 403,
                    'Error' : eror, 
                    'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*'
                    },
                    'Message': 'Reduce your token count'
            }
    except Exception as identifier:
        return {'statusCode': 500,
                'Error' : identifier, 
                'headers': {
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'Message': 'Internal Server Error'       
        }
