style: SHELL:=/usr/bin/env bash
style:
	@if ! type "sass" > /dev/null; then	\
		echo "NO SASS";										\
		exit 1;														\
	fi;																	\
	sass styles/style.scss styles/style.css --style compressed
