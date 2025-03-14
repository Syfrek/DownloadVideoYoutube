import yt_dlp

def download_video(url, output_path="."):
    try:
        ydl_opts = {
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "format": "best"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Téléchargement terminé !")
    except Exception as e:
        print(f"Erreur : {e}")
    input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    download_video(video_url)
