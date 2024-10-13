Para crear un Proyecto echo en Django
este es el orden correcto de realizarlo

1 ) Abrir el editor de codigo de su preferencia, abrir la carpeta que va a contener todo su proyecto, esa carpeta debe estar vacia, si encuentra archivos,
que ud no agrego, no los valla a borrar que son propios del editor de codigo.

Empezamos

2 ) Abrir la terminar del editor de codigo que tenga configurado con el CMD osea el Command Prompt, alli mismo sale el nombre, si trabajan con PowerShell deberia configurarlo antes, ya que hay algunas ocaciones donde no lo configuran bien, entonces en este caso veremos con el CMD de la propia terminal del editor de codigo.

3 ) Creacion del entorno virtual
        Comando para la creacion del entorno virtual
            python -m venv ( nombre del entorno virtual )
                lo comun de nombres de los entornos virtuales son venv o .venv
                    por ultimo fijarse en la terminal que debe salirle del lado izquiero algo asi
                        (.venv) C:\Users\
                            sin el entornos virtual es asi
                                C:\Users\
                                    fijarse en el entorno virtual este activo, en ocaciones les saldra una notificacion propia del editor
                                        que aunque no se vea el (.venv) esta activo, de preferencia fijencia que si o si se muestre (.venv)
                                            Comando para activar el entorno virtual en caso de que se les desactive, ya que el editor por lo general
                                                de manera automatica reconoce el entorno virtual, pero hay caso donde NO lo hace asi que aqui les dejo
                                                    el comando de activacion
                                                        .\( nombre del entorno virtual )\Scripts\active
                                                            deberia verse algo asi .\.venv\Scripts\active
                                                                una vez ya terminado la creacion del entorno virtual
                                                                    con este comando
                                                                        python -m venv ( nombre del entorno virtual )

4 ) Comando para la instalacion de Django, fijarse que el entorno virtual este activo y como saben si esta acrtivo en su terminar debe ver asi
       (.venv) C:\Users\
           pip install django

5 ) Comando para crear projecto de Django
        django-admin startproject ( nombre del proyecto ) y terminas con un ESPACIO y un ( . ) asi deberia quedar
            django-admin startproject Proyecto_Django .
                el punto final sirve para no generar doble carpeta, por eso fundamental el punto al fnal

6 ) Comando para crear aplicaciones de Django
        django-admin startapp ( nombre de la aplicaciones )
            se debe ver algo asi
                django-admin startapp App_Django

Comandos adicionales

7 ) Comando para crear directorios o carpeta como uds las conozcan o folder en ingles
        mkdir BackEnd
            asi debe verse
                (.venv) C:\Users\ingja\PycharmProjects\Clinic>mkdir BackEnd
                    la creacion de folder no importa si el entorno virtual esta o no activo da igual es un comando general sin depender de nada el mkdir
                        comando para el CMD de Windows

8 ) Comando para crear archivos de cualquier tipo
        echo. > Readme.txt
            asi debe verse
               (.venv) C:\Users\ingja\PycharmProjects\Clinic>echo. > Readme.txt
                     la creacion de archivos no importa si el entorno virtual esta o no activo da igual es un comando general sin depender de nada el mkdir
                        comando para el CMD de Windows

9 ) Comando para mover directorios o archivos de cualquier a otros directorios
        en este caso les recomiendo que las aplicaciones de django las muevan dentro de un directorio contenedor de aplicaciones
            llamado Apps y ese directorio dentro de otro directorio llamado BackEnd
                entonces seria asi
                    mkdir BackEnd
                        mkdir Apps
                            comando para poder mover el directorio Apps que esta a raiz de mi carpeta principal, moverlo adentro del directorio BackEnd
                                move ( Nombre del directorio que se va a mover ) BackEnd
                                    quedaria asi
                                        move Apps BackEnd
                                            y listo asi se paso el directorio Apps dentro del directorio BackEnd
                                                y ahora pasar una aplicacion de Django adentro del directorio Apps
                                                    seria el mismo paso asi
                                                        move App_Django BackEnd/Apps
