1. Czy pody sa zdrowe, nie crashuja
2. Nie ma bledow w logach
3. Czy nie trwa to za dlugo
---
BlueGreen-
1. Kubectl apply -f(green, blue and svc)
2. kubectl describe svc nginx-service -> sprawdzamy wersje(blue)
3. kubectl port-forward svc/nginx-service 8080:80
curl http://localhost:8080 -> sprawdzamy czy aplikacja dziala przez svc
4. kubectl get pods -l version=green
kubectl port-forward deployment/nginx-green 8081:80
curl http://localhost:8081 -> test green bez przelaczania svc
5. Zmiana version w svc z blue na green i wdrozenie go
6. Jesli wszystko dziala usuniecie blue
---
Canary-
1. Mamy sobie glowny deploy dzialajacy poprawnie i stabilnie np 5 replik
2. Wdrazamy canary z np 1 replika (czyli 20%)
3. Sprawdzamy czy pod dziala (readiness, livensess,logi,describe)
4. Zwiekszamy canary np do 40-60 procent
5. Jesli wszystko dziala to usuwamy stary deploy

Kryteria: 
-wszystkie canary pody ready
-brak bledow przez 10 min 
-smoke test poprawny-mozna wejsc na strone --->roll forward

