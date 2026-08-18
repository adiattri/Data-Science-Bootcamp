import logging

##logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} ={result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"Adding {a}-{b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Adding {a}*{b} = {result}")
    return result

add(10,15)
sub(15,10)
multiply(10,20)


