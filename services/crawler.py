import requests
from bs4 import BeautifulSoup


def scrape_card_details(card_url: str):
    """Manually scrape information from Find Your Visa Card https://usa.visa.com/pay-with-visa/find-card/,
    Visa Credit Cards: https://usa.visa.com/api/cards/creditcard/cards,
    Visa Debit Cards: https://usa.visa.com/api/cards/debit,
    Visa Prepaid Cards: https://usa.visa.com/api/cards/prepaid,
    Visa Gift Cards: https://usa.visa.com/api/cards/gift
    """

    page = requests.get(card_url)

    # credit_card = credit_card_process(page)
    # for card in credit_card:
    #     print(card)

    # debit_card = debit_card_process(page)
    # for card in debit_card:
    #     print(card)

    # prepay_card = prepay_card_process(page)
    # for card in prepay_card:
    #     print(card)

    # gift_card = gift_card_process(page)
    # for card in gift_card:
    #     print(card)

def credit_card_process(page):
    credit_card = []
    products = page.json()['products']
    for product in products:
        card_detail = product['attributes']
        card = {'cardName': BeautifulSoup(card_detail['cardName_br'], "lxml").get_text(),
                'regularApr': BeautifulSoup(card_detail['regularAprDisplay_br'], "lxml").get_text().replace('\xa0',
                                                                                                            ' '),
                'annualFee': card_detail['annualFeeDisplayPrimary'],
                'introPurchaseApr': card_detail['introAprDisplay_br'],
                'balanceTransferIntroApr': card_detail['balanceTransferIntroAprDisplayPrimary'],
                'cardIssuer': card_detail['advertiserName_br'], 'creditRating': card_detail['creditNeededVisa'],
                'featuredBenefits': BeautifulSoup(BeautifulSoup(card_detail['bullets_br'], "lxml").get_text(),
                                                  "lxml").get_text()}
        credit_card.append(card)
    return credit_card


def debit_card_process(page):
    debit_card = []
    products = page.json()
    for product in products:
        card_detail = product['attributes']
        if 'cardName_debit' in card_detail:
            card = {'cardName': BeautifulSoup(BeautifulSoup(card_detail['cardName_debit'], "lxml").get_text(),
                                              "lxml").get_text(),
                    'featuredBenefits': BeautifulSoup(
                        BeautifulSoup(card_detail['description_debit'], "lxml").get_text(), "lxml").get_text()}
            debit_card.append(card)
    return debit_card


def prepay_card_process(page):
    prepay_card = []
    products = page.json()
    for product in products:
        card_detail = product['attributes']
        card = {'cardName': BeautifulSoup(BeautifulSoup(card_detail['cardName_prepaid'], "lxml").get_text(),
                                          "lxml").get_text(),
                'featuredBenefits':
                    BeautifulSoup(card_detail['description_prepaid'], "lxml").get_text()}
        prepay_card.append(card)
    return prepay_card


def gift_card_process(page):
    gift_card = []
    products = page.json()
    for product in products:
        card_detail = product['attributes']
        card = {'cardName': BeautifulSoup(card_detail['cardName_gift'], "lxml").get_text(),
                'featuredBenefits': BeautifulSoup(
                    BeautifulSoup(card_detail['description_gift'], "lxml").get_text(), "lxml").get_text()}
        gift_card.append(card)
    return gift_card

scrape_card_details('https://usa.visa.com/api/cards/gift')
