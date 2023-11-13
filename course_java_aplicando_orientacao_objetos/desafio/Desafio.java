public class Desafio
{
    public static void main(String[] args)
    {
        Música música = new Música();

        música.setTítulo("Título de uma música");
        System.out.println(música.getTítulo());

        música.setDuraçãoEmSegundos(180);
        System.out.println(música.getDuraçãoEmSegundos());

        música.curtir();
        música.curtir();
        música.curtir();

        música.reproduzir();
        música.reproduzir();

        música.setArtista("Artista de uma música");
        System.out.println(música.getArtista());

        Podcast podcast = new Podcast();

        podcast.setTítulo("Título de um podcast");
        System.out.println(podcast.getTítulo());

        podcast.setDuraçãoEmSegundos(3600);
        System.out.println(podcast.getDuraçãoEmSegundos());

        podcast.curtir();
        podcast.curtir();

        podcast.reproduzir();
        podcast.reproduzir();
        podcast.reproduzir();

        podcast.setApresentador("Apresentador de um podcast");
        System.out.println(podcast.getApresentador());
    }
}
