# Chirp

Chirp is a calendar that stores its data in organized Markdown files. It is intended to simplify managing events, plans, alerts, todo lists, and more.

## Usage

Each day corresponds to a single file containing Markdown with optional directives. While running Chirp maintains the calendar data as a hierarchy of directories corresponding to years (`YYYY`), months (`MM`), and then the Markdown files themselves (`DD.md`).

Within the Markdown for each day there are directives that can indicate the time of day, specify alert levels, and more. 

## Examples

The command line interface is used to configure Chirp. 

With no optional parameters Vhirp will run as an ephemeral process, iterating once over all days to return a summary.

```

python chirp.py

```

This displays unfinished tasks across the past 10 days:

```

python chirp.py -10  

```

To alert in real-time Chirp must run as a daemon, as below:

```

python chirp.py --daemon

```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

