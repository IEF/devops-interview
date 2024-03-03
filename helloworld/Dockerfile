FROM eclipse-temurin:21.0.2_13-jdk-jammy AS build

RUN mkdir /src
WORKDIR /src

COPY . /src/

RUN ./gradlew clean build

FROM eclipse-temurin:21.0.2_13-jre-jammy

RUN mkdir -p /app

COPY --from=build /src/build/libs/helloworld.jar /app/

ENTRYPOINT ["java","-jar","/app/helloworld.jar"]