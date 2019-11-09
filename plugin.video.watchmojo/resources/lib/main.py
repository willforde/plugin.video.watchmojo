# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# noinspection PyUnresolvedReferences
from codequick import Route, Listitem, run


@Route.register
def root(_):
    # Add links to watchmojo youtube channels
    yield Listitem.youtube("UCaWd5_7JhbQBe4dknZhsHJg", label="WatchMojo")
    yield Listitem.youtube("UCMm0YNfHOCA-bvHmOBSx-ZA", label="WatchMojo UK")
    yield Listitem.youtube("UC9_eukrzdzY91jjDZm62FXQ", label="MojoTravels")
    yield Listitem.youtube("UC4HnC-AS714lT2TCTJ-A1zQ", label="MojoPlays")
    yield Listitem.youtube("UC88y_sxutS1mnoeBDroS74w", label="MojoTalks")
    yield Listitem.youtube("UC3rLoj87ctEHCcS7BuvIzkQ", label="MsMojo")
    yield Listitem.youtube("UCYJyrEdlwxUu7UwtFS6jA_Q", label="UnVeiled")
