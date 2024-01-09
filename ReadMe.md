Cette application web facilite l'analyse visuelle pour calculer pageRank d'une page , les graphes définis dans des fichiers XML. Elle offre une interface utilisateur simple pour interagir avec ces graphes. Voici le concept clé de l'application :

1. **Page d'Accueil (`/home`) :**

   - L'utilisateur est dirigé vers une page d'accueil où il peut choisir de télécharger un fichier XML représentant un graphe.

2. **Traitement du Fichier XML (`/` - Route `upload_xml`) :**

   - L'utilisateur sélectionne un fichier XML à télécharger via un formulaire sur la page d'accueil.
   - L'application vérifie si le fichier est au format XML.
   - Si le fichier est valide, les données du graphe sont extraites à partir du fichier XML, et un objet de graphe orienté (DiGraph) est construit à l'aide de la bibliothèque NetworkX.
   - Le PageRank du graphe est calculé à l'aide de l'algorithme de PageRank de NetworkX (`nx.pagerank`).
   - Les informations du graphe, les détails des nœuds, et les valeurs du PageRank sont ensuite transmis à une page de résultats pour affichage.

3. **Page de Résultats (`result.html`) :**

   - Cette page affiche les détails du graphe, y compris les nœuds et les arêtes.
   - Elle présente également les valeurs de PageRank associées à chaque nœud du graphe.

4. **Exécution de l'Application :**
   - L'application est exécutée localement sur le serveur Flask et peut être accédée via le navigateur web.
   - Elle offre une interface conviviale pour télécharger, explorer, et analyser des fichiers XML représentant des graphes.

Voir quelque image explicatif pour cette application dans le dossier Projet_images
