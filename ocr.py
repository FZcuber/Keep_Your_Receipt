import os
# Insert g-cloud credentials here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= None

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')

    ret = texts[0].description.split('\n')

    for text in texts:
        # print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return ret





def process(parsed):
    ids = []
    prices = []
    for i in range(len(parsed)):
        token = parsed[i]
        first = token.split()[0]
        if first.isnumeric() and len(first) == 9:
            ids.append(first)
        elif len(token) > 1 and token[0] == "$":
            add = True
            for ind in range(5):
                if "AID" in parsed[i+ind]:
                    add = False
            if add:
                prices.append(token)
    print(len(ids), len(prices))

    return dict(list(zip(ids, prices)))

if __name__ == '__main__':
    parsed = detect_text('receipt.png')
    print(process(parsed))
