SET(TARGET_NAME app_sdk)

PROJECT(${TARGET_NAME})

INCLUDE_DIRECTORIES(
    ${PROJECT_SOURCE_DIR}/
    ${PROJECT_SOURCE_DIR}/../
    ${PROJECT_SOURCE_DIR}/../tool_kits/
    ${PROJECT_SOURCE_DIR}/../include/
)

FILE(GLOB_RECURSE APP_SDK_SOURCE *.cc *.h *.cpp *.c)

ADD_LIBRARY(${TARGET_NAME} STATIC ${APP_SDK_SOURCE})
