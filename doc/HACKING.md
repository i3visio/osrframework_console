Contributing to OSRFramework Console
====================================

Reporting issues, bugs and fresh ideas
--------------------------------------

The way in which we track the issues regarding the software is by means of the
issues page in Github's project site, which can be found here:
<https://github.com/i3visio/osrframework_console/issues>.
Whether you have experimented problems with the installation, you have found a
bug in a transform or entity, you can find the place to report them there. The
only "rule" is to notify one error per issue to be able to track the problems
independently, as well as trying to provide as much information as possible
regarding the OS and package version you are using.

Contributing code
-----------------

If you want us to include your own wrapper, you will be able to extend the whole
framework. Think about the wrapper Whether you want to add a new wrapper or fix
a bug, the basic instructions to contribute and perform a pull request on Github
are the following (we assume that you have installed Git by yourself, so please
follow the instructions in the project's website to install it on your system
<https://git-scm.com/downloads>). We will assume that the username for this test
is `osrframework_contributor`.

First of all, logged in Github and fork the repository by pressing the
corresponding button in <https://github.com/i3visio/osrframework_console>. This
will create a copy of the repository under your profile (i. e.:
`https://github.com/osrframework_contributor/osrframework_console`).

You can clone your forked repository now:
```
# This is an example! Change "osrframework_contributor" for your nick!
git clone https://github.com/osrframework_contributor/osrframework_console
cd osrframework_console
```

Then, you can modify any file you want, for example, adding the new wrapper that
you have created in the previous case. Whenever you want, you can add the
changes performed to the Git index to keep track of what you have changed and
prepare it for the commit.
```
# Add one file
git add ./<YOUR_FILE>
# Or adding all the files modified... Just be a little bit more careful
# git add -A
```

Once you are happy with the changes (and you have tested them!), you can commit
the changes with a descriptive message.
```
git commit -m "Adding a new wrapper as example.py."
```

You have to push the changes to your Github project.
```
git push origin
```

You're almost there. You can now go to your project's website
(`http://github.com/osrframework_contributor/osrframework_console`) and click in
the `Pulls` tab or going directly to it by appending `pulls` to your forked URL,
something similar to
`https://github.com/osrframework_contributor/osrframework_console/pulls`. Then
provide there as much detail as you can about the contents of the pull request
and shortly we will evaluate the changes and pushed it upstream.

Style guide
-----------

Just a few things to be taken into account:
* Use four spaces '    ' instead of a tab for identing blocks.
* Provide useful and not trivial comments in English to the code you write.
* Classes should start with a capitalised initial letter.

Licensing
---------

The only thing we expect from other authors'code is to use a GPL-compatible
license for their code, preferably AGPLv3+ itself. We hope that anybody can use
this tool for free (as in Free Software Foundation's four freedoms, not as in
*free beer*), so help us to do it.
