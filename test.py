import sys
from pathlib import Path
# Agregar el directorio 'src' al sys.path
sys.path.append(str(Path(__file__).resolve().parent / 'src/module'))
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from module2 import extract_features 

texto = '<div class="ui-pdp-container__row ui-pdp-component-list"><div class="ui-pdp-container__col col-2 ui-vip-core-container--short-description ui-vip-core-container--column__right"><div class="ui-pdp-container__row ui-pdp-container__row--header" id="header"><div class="ui-pdp-header"><div class="ui-pdp-header__subtitle"><span class="ui-pdp-subtitle">Departamento en Venta</span></div><div class="ui-pdp-header__title-container"><h1 class="ui-pdp-title">2d+2b+e+b. Metro Inés De Suárez. Providencia</h1><form action="/p/MLC1499095639/bookmark/add/MLC1499095639" class="ui-pdp-bookmark ui-pdp-bookmark__link-bookmark" method="post"><input name="_csrf" type="hidden"/><button aria-checked="false" class="ui-pdp-bookmark__link-bookmark" role="switch" type="submit"><svg class="ui-pdp-icon ui-pdp-icon--bookmark ui-pdp-bookmark__icon-bookmark" height="20" viewbox="0 0 22 20" width="22" xmlns="http://www.w3.org/2000/svg"><g fill-rule="evenodd"><use href="#bookmark"></use></g></svg><svg class="ui-pdp-icon ui-pdp-icon--bookmark ui-pdp-bookmark__icon-bookmark-fill" height="20" viewbox="0 0 22 20" width="22" xmlns="http://www.w3.org/2000/svg"><g fill-rule="evenodd"><use href="#bookmark"></use></g></svg><small class="ui-pdp-bookmark__label"><span class="andes-visually-hidden">Agregar a favoritos</span></small></button></form></div><div class="ui-pdp-seller-validated"><p class="ui-pdp-color--GRAY ui-pdp-size--XSMALL ui-pdp-family--REGULAR ui-pdp-seller-validated__title">Publicado hace 1 día por <a data-testid="action" href="https://tienda.mercadolibre.cl/remax-select" target="_self">Re/max Select</a><svg class="ui-pdp-icon ui-pdp-seller-validated__icon" height="14" viewbox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><use href="#verified_small"></use></svg></p></div></div></div><div class="ui-pdp-container__row ui-pdp-container__row--price" id="price"><div class="ui-pdp-price mt-16 ui-pdp-price--size-large"><div class="ui-pdp-price__main-container"><div class="ui-pdp-price__second-line"><span data-testid="price-part"><span aria-label="5900 unidades de fomento" aria-roledescription="Precio" class="andes-money-amount ui-pdp-price__part andes-money-amount--cents-comma andes-money-amount--compact" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer" role="img" style="font-size:36px"><meta content="5900" itemprop="price"/><span aria-hidden="true" class="andes-money-amount__currency-symbol" itemprop="priceCurrency">UF</span><span aria-hidden="true" class="andes-money-amount__fraction">5.900</span></span></span></div><div class="ui-pdp-price__subtitles"><p class="ui-pdp-color--GRAY ui-pdp-size--XSMALL ui-pdp-family--REGULAR"><span data-testid="price-part"><span aria-label="221696122 pesos" aria-roledescription="Precio" class="andes-money-amount ui-pdp-price__part andes-money-amount--cents-comma andes-money-amount--compact" role="img" style="font-size:14px"><span aria-hidden="true" class="andes-money-amount__currency-symbol">$</span><span aria-hidden="true" class="andes-money-amount__fraction">221.696.122</span></span></span></p></div></div></div></div><div class="ui-pdp-container__row ui-pdp-container__row--maintenance-fee-vis" id="maintenance_fee_vis"><p class="ui-pdp-color--GRAY ui-pdp-size--XSMALL ui-pdp-family--REGULAR ui-pdp-maintenance-fee-ltr">Gastos comunes aproximados $ 120.000</p></div><div class="ui-pdp-container__row ui-pdp-container__row--grouped-main-actions" id="grouped_main_actions"><div class="ui-pdp-container-actions"><form class="ui-pdp-actions" method="get"><input name="_csrf" type="hidden" value="RaeYgFlB-PbEtlE1JvO_2bGkpy1qI65wXaGQ"/><div class="ui-pdp-actions__container"><div class="ui-pdp-action-container-request-modal"><button class="andes-button ui-vip-modal-request-button andes-button--large andes-button--loud" id=":R1aqmom9im:" type="primary"><span class="andes-button__content">Contactar</span></button></div><button class="andes-button ui-vip-action-contact-info andes-button--large andes-button--quiet" id=":R1cqmom9im:" type="secondary"><span class="andes-button__content"><svg class="ui-pdp-icon ui-pdp-icon--whatsapp ui-pdp-color--BLUE" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><use href="#whatsapp"></use></svg>WhatsApp</span></button><input name="quantity" type="hidden" value="1"/></div></form><div class="ui-pdp-recaptcha-v3"></div></div></div><div class="ui-pdp-container__row ui-pdp-container__row--report-problem" id="report_problem"><div class="ui-pdp-report-problem__property-link"><p class="ui-pdp-color--GRAY ui-pdp-size--XSMALL ui-pdp-family--REGULAR">¿Tuviste un problema con la publicación? </p><a class="ui-pdp-media__action" href="https://www.portalinmobiliario.com/noindex/denounce?item_id=MLC1499095639&amp;element_type=ITM" target="_blank">Avísanos.</a></div></div><div class="ui-pdp-container__row ui-pdp-container__row--grouped-share-bookmark" id="grouped_share_bookmark"><div class="ui-vpp-grouped-share-bookmark"><form action="/p/undefined/bookmark/add/undefined" class="ui-pdp-bookmark ui-pdp-bookmark__link-bookmark" method="post"><input name="_csrf" type="hidden"/><button aria-checked="false" class="ui-pdp-bookmark__link-bookmark" role="switch" type="submit"><svg class="ui-pdp-icon ui-pdp-icon--bookmark ui-pdp-bookmark__icon-bookmark" height="20" viewbox="0 0 22 20" width="22" xmlns="http://www.w3.org/2000/svg"><g fill-rule="evenodd"><use href="#bookmark"></use></g></svg><svg class="ui-pdp-icon ui-pdp-icon--bookmark ui-pdp-bookmark__icon-bookmark-fill" height="20" viewbox="0 0 22 20" width="22" xmlns="http://www.w3.org/2000/svg"><g fill-rule="evenodd"><use href="#bookmark"></use></g></svg><small class="ui-pdp-bookmark__label"><span class="andes-visually-hidden">Agregar a favoritos</span></small></button></form><div class="ui-pdp-share"><a class="ui-pdp-share__link" href="/share" title="Compartir"><svg class="ui-pdp-icon ui-pdp-icon--share" height="20" viewbox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><use href="#share"></use></svg><span class="ui-pdp-share__link__label">Compartir</span></a></div></div></div></div></div>'
print(extract_features(texto))
