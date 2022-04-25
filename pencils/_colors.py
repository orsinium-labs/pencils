from __future__ import annotations
from enum import Enum
from random import choice
from ._color import Color


class Colors(Enum):
    @classmethod
    def random_color(cls) -> Color:
        return choice(list(cls)).value  # type: ignore


class DefoColors(Colors):
    turquoise = Color(name="Turquoise", hex="1abc9c")
    emerald = Color(name="Emerald", hex="2ecc71")
    peter_river = Color(name="Peter river", hex="3498db")
    amethyst = Color(name="Amethyst", hex="9b59b6")
    wet_asphalt = Color(name="Wet Asphalt", hex="34495e")
    green_sea = Color(name="Green Sea", hex="16a085")
    nephritis = Color(name="Nephritis", hex="27ae60")
    belize_hole = Color(name="Belize Hole", hex="2980b9")
    wisteria = Color(name="Wisteria", hex="8e44ad")
    midnight_blue = Color(name="Midnight Blue", hex="2c3e50")
    sun_flower = Color(name="Sun Flower", hex="f1c40f")
    carrot = Color(name="Carrot", hex="e67e22")
    alizarin = Color(name="Alizarin", hex="e74c3c")
    clouds = Color(name="Clouds", hex="ecf0f1")
    concrete = Color(name="Concrete", hex="95a5a6")
    orange = Color(name="Orange", hex="f39c12")
    pumpkin = Color(name="Pumpkin", hex="d35400")
    pomegranate = Color(name="Pomegranate", hex="c0392b")
    silver = Color(name="Silver", hex="bdc3c7")
    asbestos = Color(name="Asbestos", hex="7f8c8d")


class USColors(Colors):
    light_greenish_blue = Color(name="Light Greenish Blue", hex="55efc4")
    faded_poster = Color(name="Faded Poster", hex="81ecec")
    green_darner_tail = Color(name="Green Darner Tail", hex="74b9ff")
    shy_moment = Color(name="Shy Moment", hex="a29bfe")
    city_lights = Color(name="City Lights", hex="dfe6e9")
    mint_leaf = Color(name="Mint Leaf", hex="00b894")
    robins_egg_blue = Color(name="Robin's Egg Blue", hex="00cec9")
    electron_blue = Color(name="Electron Blue", hex="0984e3")
    exodus_fruit = Color(name="Exodus Fruit", hex="6c5ce7")
    soothing_breeze = Color(name="Soothing Breeze", hex="b2bec3")
    sour_lemon = Color(name="Sour Lemon", hex="ffeaa7")
    first_date = Color(name="First Date", hex="fab1a0")
    pink_glamour = Color(name="Pink Glamour", hex="ff7675")
    pico_8_pink = Color(name="Pico-8 Pink", hex="fd79a8")
    american_river = Color(name="American River", hex="636e72")
    bright_yarrow = Color(name="Bright Yarrow", hex="fdcb6e")
    orangeville = Color(name="Orangeville", hex="e17055")
    chi_gong = Color(name="Chi-Gong", hex="d63031")
    prunus_avium = Color(name="Prunus Avium", hex="e84393")
    dracula_orchid = Color(name="Dracula Orchid", hex="2d3436")


class AUColors(Colors):
    beekeeper = Color(name="Beekeeper", hex="f6e58d")
    spiced_nectarine = Color(name="Spiced Nectarine", hex="ffbe76")
    pink_glamour = Color(name="Pink Glamour", hex="ff7979")
    june_bud = Color(name="June Bud", hex="badc58")
    coastal_breeze = Color(name="Coastal Breeze", hex="dff9fb")
    turbo = Color(name="Turbo", hex="f9ca24")
    quince_jelly = Color(name="Quince Jelly", hex="f0932b")
    carmine_pink = Color(name="Carmine Pink", hex="eb4d4b")
    pure_apple = Color(name="Pure Apple", hex="6ab04c")
    hint_of_ice_pack = Color(name="Hint of Ice Pack", hex="c7ecee")
    middle_blue = Color(name="Middle Blue", hex="7ed6df")
    heliotrope = Color(name="Heliotrope", hex="e056fd")
    exodus_fruit = Color(name="Exodus Fruit", hex="686de0")
    deep_koamaru = Color(name="Deep Koamaru", hex="30336b")
    soaring_eagle = Color(name="Soaring Eagle", hex="95afc0")
    greenland_green = Color(name="Greenland Green", hex="22a6b3")
    steel_pink = Color(name="Steel Pink", hex="be2edd")
    blurple = Color(name="Blurple", hex="4834d4")
    deep_cove = Color(name="Deep Cove", hex="130f40")
    wizard_grey = Color(name="Wizard Grey", hex="535c68")


class GBColors(Colors):
    protoss_pylon = Color(name="Protoss Pylon", hex="00a8ff")
    periwinkle = Color(name="Periwinkle", hex="9c88ff")
    rise_n_shine = Color(name="Rise-N-Shine", hex="fbc531")
    download_progress = Color(name="Download Progress", hex="4cd137")
    seabrook = Color(name="Seabrook", hex="487eb0")
    vanadyl_blue = Color(name="Vanadyl Blue", hex="0097e6")
    matt_purple = Color(name="Matt Purple", hex="8c7ae6")
    nanohanacha_gold = Color(name="Nanohanacha Gold", hex="e1b12c")
    skirret_green = Color(name="Skirret Green", hex="44bd32")
    naval = Color(name="Naval", hex="40739e")
    nasturcian_flower = Color(name="Nasturcian Flower", hex="e84118")
    lynx_white = Color(name="Lynx White", hex="f5f6fa")
    blueberry_soda = Color(name="Blueberry Soda", hex="7f8fa6")
    mazarine_blue = Color(name="Mazarine Blue", hex="273c75")
    blue_nights = Color(name="Blue Nights", hex="353b48")
    harley_davidson_orange = Color(name="Harley Davidson Orange", hex="c23616")
    hint_of_pensive = Color(name="Hint of Pensive", hex="dcdde1")
    chain_gang_grey = Color(name="Chain Gang Grey", hex="718093")
    pico_void = Color(name="Pico Void", hex="192a56")
    electromagnetic = Color(name="Electromagnetic", hex="2f3640")


class CAColors(Colors):
    jigglypuff = Color(name="Jigglypuff", hex="ff9ff3")
    casandora_yellow = Color(name="Casandora Yellow", hex="feca57")
    pastel_red = Color(name="Pastel Red", hex="ff6b6b")
    megaman = Color(name="Megaman", hex="48dbfb")
    wild_caribbean_green = Color(name="Wild Caribbean Green", hex="1dd1a1")
    lian_hong_lotus_pink = Color(name="Lián Hóng Lotus Pink", hex="f368e0")
    double_dragon_skin = Color(name="Double Dragon Skin", hex="ff9f43")
    amour = Color(name="Amour", hex="ee5253")
    cyanite = Color(name="Cyanite", hex="0abde3")
    dark_mountain_meadow = Color(name="Dark Mountain Meadow", hex="10ac84")
    jade_dust = Color(name="Jade Dust", hex="00d2d3")
    joust_blue = Color(name="Joust Blue", hex="54a0ff")
    nasu_purple = Color(name="Nasu Purple", hex="5f27cd")
    light_blue_ballerina = Color(name="Light Blue Ballerina", hex="c8d6e5")
    fuel_town = Color(name="Fuel Town", hex="576574")
    aqua_velvet = Color(name="Aqua Velvet", hex="01a3a4")
    bleu_de_france = Color(name="Bleu De France", hex="2e86de")
    bluebell = Color(name="Bluebell", hex="341f97")
    storm_petrel = Color(name="Storm Petrel", hex="8395a7")
    imperial_primer = Color(name="Imperial Primer", hex="222f3e")


class CNColors(Colors):
    golden_sand = Color(name="Golden Sand", hex="eccc68")
    coral = Color(name="Coral", hex="ff7f50")
    wild_watermelon = Color(name="Wild Watermelon", hex="ff6b81")
    peace = Color(name="Peace", hex="a4b0be")
    grisaille = Color(name="Grisaille", hex="57606f")
    orange = Color(name="Orange", hex="ffa502")
    bruschetta_tomato = Color(name="Bruschetta Tomato", hex="ff6348")
    watermelon = Color(name="Watermelon", hex="ff4757")
    bay_wharf = Color(name="Bay Wharf", hex="747d8c")
    prestige_blue = Color(name="Prestige Blue", hex="2f3542")
    lime_soap = Color(name="Lime Soap", hex="7bed9f")
    french_sky_blue = Color(name="French Sky Blue", hex="70a1ff")
    saturated_sky = Color(name="Saturated Sky", hex="5352ed")
    white = Color(name="White", hex="ffffff")
    city_lights = Color(name="City Lights", hex="dfe4ea")
    ufo_green = Color(name="UFO Green", hex="2ed573")
    clear_chill = Color(name="Clear Chill", hex="1e90ff")
    bright_greek = Color(name="Bright Greek", hex="3742fa")
    anti_flash_white = Color(name="Anti-Flash White", hex="f1f2f6")
    twinkle_blue = Color(name="Twinkle Blue", hex="ced6e0")


class NLColors(Colors):
    sunflower = Color(name="Sunflower", hex="FFC312")
    energos = Color(name="Energos", hex="C4E538")
    blue_martina = Color(name="Blue Martina", hex="12CBC4")
    lavender_rose = Color(name="Lavender Rose", hex="FDA7DF")
    bara_red = Color(name="Bara Red", hex="ED4C67")
    radiant_yellow = Color(name="Radiant Yellow", hex="F79F1F")
    android_green = Color(name="Android Green", hex="A3CB38")
    mediterranean_sea = Color(name="Mediterranean Sea", hex="1289A7")
    lavender_tea = Color(name="Lavender Tea", hex="D980FA")
    very_berry = Color(name="Very Berry", hex="B53471")
    puffins_bill = Color(name="Puffins Bill", hex="EE5A24")
    pixelated_grass = Color(name="Pixelated Grass", hex="009432")
    merchant_marine_blue = Color(name="Merchant Marine Blue", hex="0652DD")
    forgotten_purple = Color(name="Forgotten Purple", hex="9980FA")
    hollyhock = Color(name="Hollyhock", hex="833471")
    red_pigment = Color(name="Red Pigment", hex="EA2027")
    turkish_aqua = Color(name="Turkish Aqua", hex="006266")
    two_thousand_leagues_under_the_sea = Color(name="20000 Leagues Under the Sea", hex="1B1464")
    circumorbital_ring = Color(name="Circumorbital Ring", hex="5758BB")
    magenta_purple = Color(name="Magenta Purple", hex="6F1E51")


class FRColors(Colors):
    flat_flesh = Color(name="Flat Flesh", hex="fad390")
    melon_melody = Color(name="Melon Melody", hex="f8c291")
    livid = Color(name="Livid", hex="6a89cc")
    spray = Color(name="Spray", hex="82ccdd")
    paradise_green = Color(name="Paradise Green", hex="b8e994")
    squash_blossom = Color(name="Squash Blossom", hex="f6b93b")
    mandarin_red = Color(name="Mandarin Red", hex="e55039")
    azraq_blue = Color(name="Azraq Blue", hex="4a69bd")
    dupain = Color(name="Dupain", hex="60a3bc")
    aurora_green = Color(name="Aurora Green", hex="78e08f")
    iceland_poppy = Color(name="Iceland Poppy", hex="fa983a")
    tomato_red = Color(name="Tomato Red", hex="eb2f06")
    yue_guang_lan_blue = Color(name="Yuè Guāng Lán Blue", hex="1e3799")
    good_samaritan = Color(name="Good Samaritan", hex="3c6382")
    waterfall = Color(name="Waterfall", hex="38ada9")
    carrot_orange = Color(name="Carrot Orange", hex="e58e26")
    jalapeno_red = Color(name="Jalapeno Red", hex="b71540")
    dark_sapphire = Color(name="Dark Sapphire", hex="0c2461")
    forest_blues = Color(name="Forest Blues", hex="0a3d62")
    reef_encounter = Color(name="Reef Encounter", hex="079992")


class DEColors(Colors):
    fusion_red = Color(name="Fusion Red", hex="fc5c65")
    orange_hibiscus = Color(name="Orange Hibiscus", hex="fd9644")
    flirtatious = Color(name="Flirtatious", hex="fed330")
    reptile_green = Color(name="Reptile Green", hex="26de81")
    maximum_blue_green = Color(name="Maximum Blue Green", hex="2bcbba")
    desire = Color(name="Desire", hex="eb3b5a")
    beniukon_bronze = Color(name="Beniukon Bronze", hex="fa8231")
    nyc_taxi = Color(name="NYC Taxi", hex="f7b731")
    algal_fuel = Color(name="Algal Fuel", hex="20bf6b")
    turquoise_topaz = Color(name="Turquoise Topaz", hex="0fb9b1")
    high_blue = Color(name="High Blue", hex="45aaf2")
    c64_ntsc = Color(name="C64 NTSC", hex="4b7bec")
    lighter_purple = Color(name="Lighter Purple", hex="a55eea")
    twinkle_blue = Color(name="Twinkle Blue", hex="d1d8e0")
    blue_grey = Color(name="Blue Grey", hex="778ca3")
    boyzone = Color(name="Boyzone", hex="2d98da")
    royal_blue = Color(name="Royal Blue", hex="3867d6")
    gloomy_purple = Color(name="Gloomy Purple", hex="8854d0")
    innuendo = Color(name="Innuendo", hex="a5b1c2")
    blue_horizon = Color(name="Blue Horizon", hex="4b6584")


class INColors(Colors):
    orchid_orange = Color(name="Orchid Orange", hex="FEA47F")
    spiro_disco_ball = Color(name="Spiro Disco Ball", hex="25CCF7")
    honey_glow = Color(name="Honey Glow", hex="EAB543")
    sweet_garden = Color(name="Sweet Garden", hex="55E6C1")
    falling_star = Color(name="Falling Star", hex="CAD3C8")
    rich_gardenia = Color(name="Rich Gardenia", hex="F97F51")
    clear_chill = Color(name="Clear Chill", hex="1B9CFC")
    sarawak_white_pepper = Color(name="Sarawak White Pepper", hex="F8EFBA")
    keppel = Color(name="Keppel", hex="58B19F")
    ship_s_officer = Color(name="Ship's Officer", hex="2C3A47")
    fiery_fuchsia = Color(name="Fiery Fuchsia", hex="B33771")
    bluebell = Color(name="Bluebell", hex="3B3B98")
    georgia_peach = Color(name="Georgia Peach", hex="FD7272")
    oasis_stream = Color(name="Oasis Stream", hex="9AECDB")
    bright_ube = Color(name="Bright Ube", hex="D6A2E8")
    magenta_purple = Color(name="Magenta Purple", hex="6D214F")
    ending_navy_blue = Color(name="Ending Navy Blue", hex="182C61")
    sasquatch_socks = Color(name="Sasquatch Socks", hex="FC427B")
    pine_glade = Color(name="Pine Glade", hex="BDC581")
    highlighter_lavender = Color(name="Highlighter Lavender", hex="82589F")


class RUColors(Colors):
    creamy_peach = Color(name="Creamy Peach", hex="f3a683")
    rosy_highlight = Color(name="Rosy Highlight", hex="f7d794")
    soft_blue = Color(name="Soft Blue", hex="778beb")
    brewed_mustard = Color(name="Brewed Mustard", hex="e77f67")
    old_geranium = Color(name="Old Geranium", hex="cf6a87")
    sawtooth_aak = Color(name="Sawtooth Aak", hex="f19066")
    summertime = Color(name="Summertime", hex="f5cd79")
    cornflower = Color(name="Cornflower", hex="546de5")
    tigerlily = Color(name="Tigerlily", hex="e15f41")
    deep_rose = Color(name="Deep Rose", hex="c44569")
    purple_mountain_majesty = Color(name="Purple Mountain Majesty", hex="786fa6")
    rogue_pink = Color(name="Rogue Pink", hex="f8a5c2")
    squeaky = Color(name="Squeaky", hex="63cdda")
    apple_valley = Color(name="Apple Valley", hex="ea8685")
    pencil_lead = Color(name="Pencil Lead", hex="596275")
    purple_corallite = Color(name="Purple Corallite", hex="574b90")
    flamingo_pink = Color(name="Flamingo Pink", hex="f78fb3")
    blue_curacao = Color(name="Blue Curacao", hex="3dc1d3")
    porcelain_rose = Color(name="Porcelain Rose", hex="e66767")
    biscay = Color(name="Biscay", hex="303952")


class ESColors(Colors):
    jacksons_purple = Color(name="Jacksons Purple", hex="40407a")
    c64_purple = Color(name="C64 Purple", hex="706fd3")
    swan_white = Color(name="Swan White", hex="f7f1e3")
    summer_sky = Color(name="Summer Sky", hex="34ace0")
    celestial_green = Color(name="Celestial Green", hex="33d9b2")
    lucky_point = Color(name="Lucky Point", hex="2c2c54")
    liberty = Color(name="Liberty", hex="474787")
    hot_stone = Color(name="Hot Stone", hex="aaa69d")
    devil_blue = Color(name="Devil Blue", hex="227093")
    palm_springs_splash = Color(name="Palm Springs Splash", hex="218c74")
    fluorescent_red = Color(name="Fluorescent Red", hex="ff5252")
    synthetic_pumpkin = Color(name="Synthetic Pumpkin", hex="ff793f")
    crocodile_tooth = Color(name="Crocodile Tooth", hex="d1ccc0")
    mandarin_sorbet = Color(name="Mandarin Sorbet", hex="ffb142")
    spiced_butternut = Color(name="Spiced Butternut", hex="ffda79")
    eye_of_newt = Color(name="Eye Of Newt", hex="b33939")
    chilean_fire = Color(name="Chilean Fire", hex="cd6133")
    grey_porcelain = Color(name="Grey Porcelain", hex="84817a")
    alameda_ochre = Color(name="Alameda Ochre", hex="cc8e35")
    desert = Color(name="Desert", hex="ccae62")


class SEColors(Colors):
    highlighter_pink = Color(name="Highlighter Pink", hex="ef5777")
    dark_periwinkle = Color(name="Dark Periwinkle", hex="575fcf")
    megaman = Color(name="Megaman", hex="4bcffa")
    fresh_turquoise = Color(name="Fresh Turquoise", hex="34e7e4")
    minty_green = Color(name="Minty Green", hex="0be881")
    sizzling_red = Color(name="Sizzling Red", hex="f53b57")
    free_speech_blue = Color(name="Free Speech Blue", hex="3c40c6")
    spiro_disco_ball = Color(name="Spiro Disco Ball", hex="0fbcf9")
    jade_dust = Color(name="Jade Dust", hex="00d8d6")
    green_teal = Color(name="Green Teal", hex="05c46b")
    nârenji_orange = Color(name="Nârenji Orange", hex="ffc048")
    yriel_yellow = Color(name="Yriel Yellow", hex="ffdd59")
    sunset_orange = Color(name="Sunset Orange", hex="ff5e57")
    hint_of_elusive_blue = Color(name="Hint of Elusive Blue", hex="d2dae2")
    good_night = Color(name="Good Night!", hex="485460")
    chrome_yellow = Color(name="Chrome Yellow", hex="ffa801")
    vibrant_yellow = Color(name="Vibrant Yellow", hex="ffd32a")
    red_orange = Color(name="Red Orange", hex="ff3f34")
    london_square = Color(name="London Square", hex="808e9b")
    black_pearl = Color(name="Black Pearl", hex="1e272e")


class TRColors(Colors):
    bright_lilac = Color(name="Bright Lilac", hex="cd84f1")
    pretty_please = Color(name="Pretty Please", hex="ffcccc")
    light_red = Color(name="Light Red", hex="ff4d4d")
    mandarin_sorbet = Color(name="Mandarin Sorbet", hex="ffaf40")
    unmellow_yellow = Color(name="Unmellow Yellow", hex="fffa65")
    light_purple = Color(name="Light Purple", hex="c56cf0")
    young_salmon = Color(name="Young Salmon", hex="ffb8b8")
    red_orange = Color(name="Red Orange", hex="ff3838")
    radiant_yellow = Color(name="Radiant Yellow", hex="ff9f1a")
    dorn_yellow = Color(name="Dorn Yellow", hex="fff200")
    wintergreen = Color(name="Wintergreen", hex="32ff7e")
    electric_blue = Color(name="Electric Blue", hex="7efff5")
    neon_blue = Color(name="Neon Blue", hex="18dcff")
    light_slate_blue = Color(name="Light Slate Blue", hex="7d5fff")
    shadowed_steel = Color(name="Shadowed Steel", hex="4b4b4b")
    weird_green = Color(name="Weird Green", hex="3ae374")
    hammam_blue = Color(name="Hammam Blue", hex="67e6dc")
    spiro_disco_ball = Color(name="Spiro Disco Ball", hex="17c0eb")
    light_indigo = Color(name="Light Indigo", hex="7158e2")
    baltic_sea = Color(name="Baltic Sea", hex="3d3d3d")


class SocialColors(Colors):
    facebook = Color(name="Facebook", hex="1877f2")
    messenger = Color(name="Messenger", hex="0099ff")
    twitter = Color(name="Twitter", hex="1da1f2")
    linkedin = Color(name="LinkedIn", hex="0a66c2")
    skype = Color(name="Skype", hex="00aff0")
    dropbox = Color(name="Dropbox", hex="0061ff")
    wordpress = Color(name="Wordpress", hex="21759b")
    vimeo = Color(name="Vimeo", hex="1ab7ea")
    slideshare = Color(name="SlideShare", hex="0077b5")
    vk = Color(name="VK", hex="4c75a3")
    tumblr = Color(name="Tumblr", hex="34465d")
    yahoo = Color(name="Yahoo", hex="410093")
    pinterest = Color(name="Pinterest", hex="bd081c")
    youtube = Color(name="Youtube", hex="cd201f")
    reddit = Color(name="Reddit", hex="ff5700")
    quora = Color(name="Quora", hex="b92b27")
    yelp = Color(name="Yelp", hex="af0606")
    weibo = Color(name="Weibo", hex="df2029")
    producthunt = Color(name="ProductHunt", hex="da552f")
    hackernews = Color(name="HackerNews", hex="ff6600")
    soundcloud = Color(name="Soundcloud", hex="ff3300")
    blogger = Color(name="Blogger", hex="f57d00")
    snapchat = Color(name="SnapChat", hex="fffc00")
    whatsapp = Color(name="WhatsApp", hex="25d366")
    wechat = Color(name="WeChat", hex="09b83e")
    line = Color(name="Line", hex="00c300")
    medium = Color(name="Medium", hex="02b875")
    vine = Color(name="Vine", hex="00b489")
    slack = Color(name="Slack", hex="3aaf85")
    instagram = Color(name="Instagram", hex="e4405f")
    dribbble = Color(name="Dribbble", hex="ea4c89")
    flickr = Color(name="Flickr", hex="ff0084")
    foursquare = Color(name="FourSquare", hex="f94877")
    tiktok = Color(name="TikTok", hex="ee1d51")
    behance = Color(name="Behance", hex="131418")


class MetroColors(Colors):
    lime = Color(name="Lime", hex="A4C400")
    green = Color(name="Green", hex="60A917")
    emerald = Color(name="Emerald", hex="008A00")
    teal = Color(name="Teal", hex="00ABA9")
    cyan = Color(name="Cyan", hex="1BA1E2")
    cobalt = Color(name="Cobalt", hex="0050EF")
    indigo = Color(name="Indigo", hex="6A00FF")
    violet = Color(name="Violet", hex="AA00FF")
    pink = Color(name="Pink", hex="F472D0")
    magenta = Color(name="Magenta", hex="D80073")
    crimson = Color(name="Crimson", hex="A20025")
    red = Color(name="Red", hex="E51400")
    orange = Color(name="Orange", hex="FA6800")
    amber = Color(name="Amber", hex="F0A30A")
    yellow = Color(name="Yellow", hex="E3C800")
    brown = Color(name="Brown", hex="825A2C")
    olive = Color(name="Olive", hex="6D8764")
    steel = Color(name="Steel", hex="647687")
    mauve = Color(name="Mauve", hex="76608A")
    sienna = Color(name="Sienna", hex="A0522D")


class CSSColors(Colors):
    aliceblue = Color(name="aliceblue", hex="f0f8ff")
    antiquewhite = Color(name="antiquewhite", hex="faebd7")
    aqua = Color(name="aqua", hex="00ffff")
    aquamarine = Color(name="aquamarine", hex="7fffd4")
    azure = Color(name="azure", hex="f0ffff")
    beige = Color(name="beige", hex="f5f5dc")
    bisque = Color(name="bisque", hex="ffe4c4")
    black = Color(name="black", hex="000000")
    blanchedalmond = Color(name="blanchedalmond", hex="ffebcd")
    blue = Color(name="blue", hex="0000ff")
    blueviolet = Color(name="blueviolet", hex="8a2be2")
    brown = Color(name="brown", hex="a52a2a")
    burlywood = Color(name="burlywood", hex="deb887")
    cadetblue = Color(name="cadetblue", hex="5f9ea0")
    chartreuse = Color(name="chartreuse", hex="7fff00")
    chocolate = Color(name="chocolate", hex="d2691e")
    coral = Color(name="coral", hex="ff7f50")
    cornflowerblue = Color(name="cornflowerblue", hex="6495ed")
    cornsilk = Color(name="cornsilk", hex="fff8dc")
    crimson = Color(name="crimson", hex="dc143c")
    cyan = Color(name="cyan", hex="00ffff")
    darkblue = Color(name="darkblue", hex="00008b")
    darkcyan = Color(name="darkcyan", hex="008b8b")
    darkgoldenrod = Color(name="darkgoldenrod", hex="b8860b")
    darkgray = Color(name="darkgray", hex="a9a9a9")
    darkgreen = Color(name="darkgreen", hex="006400")
    darkgrey = Color(name="darkgrey", hex="a9a9a9")
    darkkhaki = Color(name="darkkhaki", hex="bdb76b")
    darkmagenta = Color(name="darkmagenta", hex="8b008b")
    darkolivegreen = Color(name="darkolivegreen", hex="556b2f")
    darkorange = Color(name="darkorange", hex="ff8c00")
    darkorchid = Color(name="darkorchid", hex="9932cc")
    darkred = Color(name="darkred", hex="8b0000")
    darksalmon = Color(name="darksalmon", hex="e9967a")
    darkseagreen = Color(name="darkseagreen", hex="8fbc8f")
    darkslateblue = Color(name="darkslateblue", hex="483d8b")
    darkslategray = Color(name="darkslategray", hex="2f4f4f")
    darkslategrey = Color(name="darkslategrey", hex="2f4f4f")
    darkturquoise = Color(name="darkturquoise", hex="00ced1")
    darkviolet = Color(name="darkviolet", hex="9400d3")
    deeppink = Color(name="deeppink", hex="ff1493")
    deepskyblue = Color(name="deepskyblue", hex="00bfff")
    dimgray = Color(name="dimgray", hex="696969")
    dimgrey = Color(name="dimgrey", hex="696969")
    dodgerblue = Color(name="dodgerblue", hex="1e90ff")
    firebrick = Color(name="firebrick", hex="b22222")
    floralwhite = Color(name="floralwhite", hex="fffaf0")
    forestgreen = Color(name="forestgreen", hex="228b22")
    fuchsia = Color(name="fuchsia", hex="ff00ff")
    gainsboro = Color(name="gainsboro", hex="dcdcdc")
    ghostwhite = Color(name="ghostwhite", hex="f8f8ff")
    goldenrod = Color(name="goldenrod", hex="daa520")
    gold = Color(name="gold", hex="ffd700")
    gray = Color(name="gray", hex="808080")
    green = Color(name="green", hex="008000")
    greenyellow = Color(name="greenyellow", hex="adff2f")
    grey = Color(name="grey", hex="808080")
    honeydew = Color(name="honeydew", hex="f0fff0")
    hotpink = Color(name="hotpink", hex="ff69b4")
    indianred = Color(name="indianred", hex="cd5c5c")
    indigo = Color(name="indigo", hex="4b0082")
    ivory = Color(name="ivory", hex="fffff0")
    khaki = Color(name="khaki", hex="f0e68c")
    lavenderblush = Color(name="lavenderblush", hex="fff0f5")
    lavender = Color(name="lavender", hex="e6e6fa")
    lawngreen = Color(name="lawngreen", hex="7cfc00")
    lemonchiffon = Color(name="lemonchiffon", hex="fffacd")
    lightblue = Color(name="lightblue", hex="add8e6")
    lightcoral = Color(name="lightcoral", hex="f08080")
    lightcyan = Color(name="lightcyan", hex="e0ffff")
    lightgoldenrodyellow = Color(name="lightgoldenrodyellow", hex="fafad2")
    lightgray = Color(name="lightgray", hex="d3d3d3")
    lightgreen = Color(name="lightgreen", hex="90ee90")
    lightgrey = Color(name="lightgrey", hex="d3d3d3")
    lightpink = Color(name="lightpink", hex="ffb6c1")
    lightsalmon = Color(name="lightsalmon", hex="ffa07a")
    lightseagreen = Color(name="lightseagreen", hex="20b2aa")
    lightskyblue = Color(name="lightskyblue", hex="87cefa")
    lightslategray = Color(name="lightslategray", hex="778899")
    lightslategrey = Color(name="lightslategrey", hex="778899")
    lightsteelblue = Color(name="lightsteelblue", hex="b0c4de")
    lightyellow = Color(name="lightyellow", hex="ffffe0")
    lime = Color(name="lime", hex="00ff00")
    limegreen = Color(name="limegreen", hex="32cd32")
    linen = Color(name="linen", hex="faf0e6")
    magenta = Color(name="magenta", hex="ff00ff")
    maroon = Color(name="maroon", hex="800000")
    mediumaquamarine = Color(name="mediumaquamarine", hex="66cdaa")
    mediumblue = Color(name="mediumblue", hex="0000cd")
    mediumorchid = Color(name="mediumorchid", hex="ba55d3")
    mediumpurple = Color(name="mediumpurple", hex="9370db")
    mediumseagreen = Color(name="mediumseagreen", hex="3cb371")
    mediumslateblue = Color(name="mediumslateblue", hex="7b68ee")
    mediumspringgreen = Color(name="mediumspringgreen", hex="00fa9a")
    mediumturquoise = Color(name="mediumturquoise", hex="48d1cc")
    mediumvioletred = Color(name="mediumvioletred", hex="c71585")
    midnightblue = Color(name="midnightblue", hex="191970")
    mintcream = Color(name="mintcream", hex="f5fffa")
    mistyrose = Color(name="mistyrose", hex="ffe4e1")
    moccasin = Color(name="moccasin", hex="ffe4b5")
    navajowhite = Color(name="navajowhite", hex="ffdead")
    navy = Color(name="navy", hex="000080")
    oldlace = Color(name="oldlace", hex="fdf5e6")
    olive = Color(name="olive", hex="808000")
    olivedrab = Color(name="olivedrab", hex="6b8e23")
    orange = Color(name="orange", hex="ffa500")
    orangered = Color(name="orangered", hex="ff4500")
    orchid = Color(name="orchid", hex="da70d6")
    palegoldenrod = Color(name="palegoldenrod", hex="eee8aa")
    palegreen = Color(name="palegreen", hex="98fb98")
    paleturquoise = Color(name="paleturquoise", hex="afeeee")
    palevioletred = Color(name="palevioletred", hex="db7093")
    papayawhip = Color(name="papayawhip", hex="ffefd5")
    peachpuff = Color(name="peachpuff", hex="ffdab9")
    peru = Color(name="peru", hex="cd853f")
    pink = Color(name="pink", hex="ffc0cb")
    plum = Color(name="plum", hex="dda0dd")
    powderblue = Color(name="powderblue", hex="b0e0e6")
    purple = Color(name="purple", hex="800080")
    rebeccapurple = Color(name="rebeccapurple", hex="663399")
    red = Color(name="red", hex="ff0000")
    rosybrown = Color(name="rosybrown", hex="bc8f8f")
    royalblue = Color(name="royalblue", hex="4169e1")
    saddlebrown = Color(name="saddlebrown", hex="8b4513")
    salmon = Color(name="salmon", hex="fa8072")
    sandybrown = Color(name="sandybrown", hex="f4a460")
    seagreen = Color(name="seagreen", hex="2e8b57")
    seashell = Color(name="seashell", hex="fff5ee")
    sienna = Color(name="sienna", hex="a0522d")
    silver = Color(name="silver", hex="c0c0c0")
    skyblue = Color(name="skyblue", hex="87ceeb")
    slateblue = Color(name="slateblue", hex="6a5acd")
    slategray = Color(name="slategray", hex="708090")
    slategrey = Color(name="slategrey", hex="708090")
    snow = Color(name="snow", hex="fffafa")
    springgreen = Color(name="springgreen", hex="00ff7f")
    steelblue = Color(name="steelblue", hex="4682b4")
    tan = Color(name="tan", hex="d2b48c")
    teal = Color(name="teal", hex="008080")
    thistle = Color(name="thistle", hex="d8bfd8")
    tomato = Color(name="tomato", hex="ff6347")
    turquoise = Color(name="turquoise", hex="40e0d0")
    violet = Color(name="violet", hex="ee82ee")
    wheat = Color(name="wheat", hex="f5deb3")
    white = Color(name="white", hex="ffffff")
    whitesmoke = Color(name="whitesmoke", hex="f5f5f5")
    yellow = Color(name="yellow", hex="ffff00")
    yellowgreen = Color(name="yellowgreen", hex="9acd32")


class TailwindColors(Colors):
    red = Color(name="Red", hex="ef4444")
    orange = Color(name="Orange", hex="f97316")
    amber = Color(name="Amber", hex="f59e0b")
    yellow = Color(name="Yellow", hex="eab308")
    lime = Color(name="Lime", hex="84cc16")
    green = Color(name="Green", hex="22c55e")
    emerald = Color(name="Emerald", hex="10b981")
    teal = Color(name="Teal", hex="14b8a6")
    cyan = Color(name="Cyan", hex="06b6d4")
    light_blue = Color(name="Light Blue", hex="0ea5e9")
    blue = Color(name="Blue", hex="3b82f6")
    indigo = Color(name="Indigo", hex="6366f1")
    violet = Color(name="Violet", hex="8b5cf6")
    purple = Color(name="Purple", hex="a855f7")
    fuchsia = Color(name="Fuchsia", hex="d946ef")
    pink = Color(name="Pink", hex="ec4899")
    rose = Color(name="Rose", hex="f43f5e")
    warm_gray = Color(name="Warm Gray", hex="78716c")
    true_gray = Color(name="True Gray", hex="737373")
    gray = Color(name="Gray", hex="71717a")
    cool_gray = Color(name="Cool Gray", hex="6b7280")
    blue_gray = Color(name="Blue Gray", hex="64748b")
