CREATE DATABASE szabadaba;

CREATE TABLE public."Image"
(
    id bigint NOT NULL,
    image bytea,
    format character varying(40),
    PRIMARY KEY (id)
);

ALTER TABLE public."Image"
    OWNER to postgres;

CREATE TABLE public."Tag"
(
    id bigint NOT NULL,
    name character varying[] NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public."Tag"
    OWNER to postgres;

CREATE TABLE public."ImageTag"
(
    id bigint NOT NULL,
    "imageId" bigint NOT NULL,
    "tagId" bigint NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public."ImageTag"
    OWNER to postgres;

CREATE TABLE public."Dataset"
(
    id bigint NOT NULL,
    name character varying[] NOT NULL,
    description character varying[] NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public."Dataset"
    OWNER to postgres;

CREATE TABLE public."ImageDataset"
(
    id bigint NOT NULL,
    "datasetId" bigint NOT NULL,
    "imageId" bigint NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public."ImageDataset"
    OWNER to postgres;