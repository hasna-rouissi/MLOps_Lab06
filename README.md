# Lab 6 : Déploiement K8s d’un système MLOps Churn
## Étape 1 : Préparer l’environnement Kubernetes
<img width="945" height="591" alt="image" src="https://github.com/user-attachments/assets/c5cb0c9a-51e0-4b9b-a3d6-9d6047874df9" />

## Étape 2 : Préparer l’image Docker de l’API churn
<img width="945" height="693" alt="image" src="https://github.com/user-attachments/assets/542af7c9-8695-44b6-a614-feb013c38429" />
<img width="945" height="327" alt="image" src="https://github.com/user-attachments/assets/0fc0d469-38f9-4f5f-807d-6b08c727b269" />

## Étape 3 : Créer le dossier des manifests Kubernetes
<img width="945" height="229" alt="image" src="https://github.com/user-attachments/assets/aec77762-9565-49c2-9f05-834ca8419964" />
<img width="841" height="566" alt="image" src="https://github.com/user-attachments/assets/5b1ef454-5c58-4ac1-a221-a651a4328017" />

## Étape 4 : Construire l’image Docker (tag versionné)
<img width="945" height="787" alt="image" src="https://github.com/user-attachments/assets/e613ed82-e507-4516-a481-7a84d1b99953" />
<img width="945" height="75" alt="image" src="https://github.com/user-attachments/assets/b9947fa4-ed3e-4944-b3c6-06bc38d8cba9" />

## Étape 5 : Charger explicitement l’image dans Minikube
<img width="945" height="156" alt="image" src="https://github.com/user-attachments/assets/f40c19e5-0b5d-43df-bf54-e9ce000aabfd" />

## Étape 6 : Deployment Kubernetes pour l’API churn
<img width="945" height="311" alt="image" src="https://github.com/user-attachments/assets/f41dce36-e8ef-4431-b014-e6be2d86a1b5" />
<img width="945" height="328" alt="image" src="https://github.com/user-attachments/assets/3638e1a0-8148-4b09-8583-2eecbed538a4" />
<img width="945" height="550" alt="image" src="https://github.com/user-attachments/assets/03869b89-ad17-48ef-8be0-b4bd0b43f720" />

## Étape 7 : Exposer l’API via un Service NodePort
<img width="942" height="209" alt="image" src="https://github.com/user-attachments/assets/e7fa6163-6fe8-4658-8d68-64857280b909" />
<img width="739" height="470" alt="image" src="https://github.com/user-attachments/assets/3f14ad87-8447-4c0a-8641-4980ef649e7f" />
<img width="945" height="425" alt="image" src="https://github.com/user-attachments/assets/b5f177f3-e130-4c39-836e-7fc20a222913" />
<img width="945" height="671" alt="image" src="https://github.com/user-attachments/assets/0da522e8-f1dc-4885-a276-60cf3b2f45df" />

## Étape 8 : Injecter la configuration MLOps via ConfigMap
<img width="945" height="267" alt="image" src="https://github.com/user-attachments/assets/a64e012e-6031-4968-9c24-11a5ded9d38f" />
<img width="788" height="308" alt="image" src="https://github.com/user-attachments/assets/f6535abc-0e77-472c-83c7-cd29cdc7fe0c" />
<img width="945" height="96" alt="image" src="https://github.com/user-attachments/assets/d19ba51f-2392-4cf0-8a6e-2b52b17e36e0" />
<img width="945" height="464" alt="image" src="https://github.com/user-attachments/assets/8dc15ce5-ad67-4fac-98a5-9302b83b5b16" />
<img width="945" height="672" alt="image" src="https://github.com/user-attachments/assets/62daacbc-775f-4a87-a3a7-e6f738b764a0" />
<img width="945" height="41" alt="image" src="https://github.com/user-attachments/assets/bdd4c8cb-e03f-4e5a-af43-3a91cc2ef01d" />
<img width="945" height="79" alt="image" src="https://github.com/user-attachments/assets/913d765e-26b3-4861-a6ac-5b38afa178f6" />
<img width="945" height="75" alt="image" src="https://github.com/user-attachments/assets/85dc8c5d-875a-4795-b4c2-234eabd0eef3" />

## Étape 9 : Gérer les secrets (MONITORING_TOKEN)
<img width="945" height="191" alt="image" src="https://github.com/user-attachments/assets/08e44022-b79c-4966-9d2d-4b0d74168cd3" />
<img width="631" height="284" alt="image" src="https://github.com/user-attachments/assets/fab95fef-c2c3-48b6-9cdf-1d9698ef1626" />
<img width="945" height="323" alt="image" src="https://github.com/user-attachments/assets/a36ea89b-4e47-46a0-8e56-8e5433015c46" />
<img width="945" height="674" alt="image" src="https://github.com/user-attachments/assets/b447a984-8ad1-46bb-ba66-47614702e594" />
<img width="945" height="131" alt="image" src="https://github.com/user-attachments/assets/4adbbc30-6c35-407a-9d39-7699c2d92b71" />

## Étape 10 : Mise en place des endpoints de santé et des probes Kubernetes pour l’API Churn
<img width="945" height="452" alt="image" src="https://github.com/user-attachments/assets/4b70a102-fe54-4e67-9276-07c9fd6948e5" />
<img width="945" height="38" alt="image" src="https://github.com/user-attachments/assets/ce91d638-e290-43f0-8337-cdf8e0faefa3" />

## Étape 11 : Ajouter les probes (liveness / readiness / startup)
<img width="945" height="571" alt="image" src="https://github.com/user-attachments/assets/679934b7-4154-41d3-9563-f1922158e51f" />
<img width="945" height="44" alt="image" src="https://github.com/user-attachments/assets/2ee777af-8dba-42b1-ac44-e3ac7bb1e35a" />
<img width="945" height="789" alt="image" src="https://github.com/user-attachments/assets/42d64ac6-c516-468a-9048-63a4731f6efc" />
<img width="945" height="736" alt="image" src="https://github.com/user-attachments/assets/5ada296c-6b83-4f0d-aff3-d6dbe20b27c0" />
<img width="945" height="134" alt="image" src="https://github.com/user-attachments/assets/e85ad10c-0113-47d1-97f4-9b289fe22466" />
<img width="838" height="120" alt="image" src="https://github.com/user-attachments/assets/13ade099-c556-4682-87bc-33a421c5bb43" />

## Étape 12 : Volume persistant pour registry + logs
<img width="908" height="231" alt="image" src="https://github.com/user-attachments/assets/548924f9-7629-4d97-9d39-42a1f15affd5" />
<img width="945" height="350" alt="image" src="https://github.com/user-attachments/assets/0b5877bc-8435-4ad2-a8aa-18a978512eab" />
<img width="945" height="92" alt="image" src="https://github.com/user-attachments/assets/dfee5d39-13cb-4f57-9918-b0709620feb2" />
<img width="945" height="233" alt="image" src="https://github.com/user-attachments/assets/092ae97b-79f7-418d-bb44-81e74bad0127" />
<img width="942" height="783" alt="image" src="https://github.com/user-attachments/assets/5092c5a7-b517-474f-a97e-9c6121f6383d" />
<img width="945" height="66" alt="image" src="https://github.com/user-attachments/assets/7aa190ed-1e41-4e17-b7c0-c535be369f85" />
<img width="849" height="477" alt="image" src="https://github.com/user-attachments/assets/d0d6321f-dfbc-4094-8a75-ece3854ed5bf" />
<img width="945" height="515" alt="image" src="https://github.com/user-attachments/assets/c3e3317e-b7b4-4619-ac3a-be3d5d4afedd" />
<img width="945" height="197" alt="image" src="https://github.com/user-attachments/assets/8967a4e3-4caa-473a-bac2-f6c1e0fcce7c" />
<img width="945" height="91" alt="image" src="https://github.com/user-attachments/assets/82305cd9-4515-4ea4-91be-0e6b58e76488" />

## Étape 13: NetworkPolicy
<img width="945" height="232" alt="image" src="https://github.com/user-attachments/assets/96cb49ef-837d-4a9f-9c24-d78d9cac11a1" />
<img width="881" height="545" alt="image" src="https://github.com/user-attachments/assets/df657bd6-5109-4b89-8fa2-7e35b233b70b" />
<img width="945" height="141" alt="image" src="https://github.com/user-attachments/assets/687a24a0-3287-45f9-8e65-e7ff64cfcac2" />

## Étape 14 : Vérifications finales
<img width="945" height="194" alt="image" src="https://github.com/user-attachments/assets/efd35af6-ef48-4a01-b569-19c9c97a8097" />
<img width="945" height="575" alt="image" src="https://github.com/user-attachments/assets/3d3b551a-a96c-4bed-ae2f-b46ffc2cd14a" />
<img width="945" height="703" alt="image" src="https://github.com/user-attachments/assets/f3636d3d-4cce-49c2-8d2a-7113b6c45744" />
<img width="945" height="175" alt="image" src="https://github.com/user-attachments/assets/915db964-3892-4f07-98b4-ff73007c3fe3" />


























