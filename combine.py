import ocr
import api.target as api_call

def weight_to_float(x):
    for i in range(1, len(x)):
        try:
            float(x[:i])
        except:
            return float(x[:i - 1])


def price_formatting(x):
    if x[0] == '$':
        return x[1:]
    return x


def get_weight(picture_file):
    from_ocr_dict = ocr.process(ocr.detect_text(picture_file))

    print(from_ocr_dict)

    results = api_call.get_info(from_ocr_dict.keys(), cache_filename='../api/cache.json')

    total_weight = 0

    for i in results:
        if i['is meat']:
            if i['is processed']:
                total_weight += weight_to_float(i['weight'])
            else:
                total_weight += float(price_formatting(from_ocr_dict[i['id']]))/float(i['price'])
    
    return total_weight




if __name__ == '__main__':
    print(get_weight('receipt3.png'))