import sys
from robobrowser import RoboBrowser


'''
Use RoboBrowser as a tool to obtain an Accessibility Testing Metric

We score a webpage on its Accessibility based on elements that it has and whether or not that content
is accessible in all ways.
'''
def accessibility_metric(url):
    # Browse to URL
    browser = RoboBrowser(history=True)
    browser.open(url)

    total = 0

    headers = browser.find_all('header')
    total += len(headers)
    header_score = check_element(headers, 'banner')

    navs = browser.find_all('nav')
    total += len(navs)
    nav_score = check_element(navs, 'navigation')

    footers = browser.find_all('footer')
    total += len(footers)
    footer_score = check_element(footers, 'contentinfo')

    asides = browser.find_all('aside')
    total += len(asides)
    aside_score = check_element(asides, 'complementary')

    score = header_score + nav_score + footer_score + aside_score

    print('\nWe found ' + str(total) + ' total elements.\nYour accessibility score is: \nACCESSIBLE ELEMENTS / TOTAL ELEMENTS')
    print('= ' + str(score) + ' / ' + str(total))
    print('= ' + str(float(score) / float(total)))
    print('\nNote: this number should be as close to 1 as possible for good accessibility.\n')

    return score


def check_element(elements, role):
    total = len(elements)
    role_count = 0

    if total == 0:
        return 0

    for element in elements:
        if element.get('role') is not None and element['role'] == role:
            role_count += 1

    return role_count / total

def main(argv):
    url = argv[0]
    print('Testing accessibility of ' + url + '\n\n')
    accessibility_metric(argv[0])
    print('Testing complete.')

if __name__ == "__main__":
   main(sys.argv[1:])
