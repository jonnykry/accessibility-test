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

    header_score = check_headers(browser)
    print(header_score)
    # check_nav()
    # check_footer()
    # check_aside()
    # check_article()

    return 0


def check_headers(browser):
    headers = browser.find_all('header')

    total = len(headers)
    role_count = 0

    for header in headers:
        role = header.role

        if role is not None and role == 'banner':
            role_count += 1

    return role_count / total

def main(argv):
    accessibility_metric(argv[0])

if __name__ == "__main__":
   main(sys.argv[1:])
