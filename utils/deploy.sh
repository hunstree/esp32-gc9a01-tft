#!/bin/bash

function transfer_file() {
    #echo "set TX_OK = ampy -p /dev/ttyUSB0 put $i $i"
    echo -n " ... "
    set TX_OK = $(ampy -p /dev/ttyUSB0 put $1 $1)
    if ( $TX_OK ); then
        echo "OK";
    else
        echo "failed"
    fi

}

if [ -e /dev/ttyUSB0 ]; then
    if [ ! -w /dev/ttyUSB0 ]; then
        echo "sudo chown gabor /dev/ttyUSB0"
        sudo chown gabor /dev/ttyUSB0
    fi
    
    readarray -s 1 PROJECT_FILES < <(cat ./.upy.project)
    LAST_DEPLOYMENT=`head -n 1 ./.upy.project`
    case $1 in
        all|ALL|All)
            LAST_DEPLOYMENT=0
        ;;
        *)
        ;;
    esac


    echo -e "`/bin/date +%s`" > ./.upy.project
    echo "Last deployment "$(/bin/date "--date=@$LAST_DEPLOYMENT")  
    for i in ${PROJECT_FILES[@]}; do
        echo -e $i >> ./.upy.project
        file_mod_time_sec=$(stat -c %Y $i)
        file_mod_time=$(stat -c %y $i)
        echo -n "$i" "$file_mod_time"
        if [[ $file_mod_time_sec -gt $LAST_DEPLOYMENT ]]; then
            transfer_file $i
        else 
            echo ""
        fi
        sleep 0.1
        
    done
    
    echo "Finished"
    #picocom /dev/ttyUSB0 -b 115200
else
    echo "/dev/ttyUSB0 does not exists"
    exit 1
fi
