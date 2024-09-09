CREATE TABLE Street(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE Location(
    id int not null primary key,
    latitude float not null,
    longitude float not null,
    street_id int not null,
    street_id int FOREIGN KEY REFERENCES Street(id)
);

CREATE TABLE Legislation(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE Ethnicity(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE Outcome(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE SearchObjective(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE SearchType(
    id int not null primary key,
    name varchar(255)
);

CREATE TABLE Operation(
    id int not null primary key,
    name varchar(255)
);


CREATE TABLE StopandSearchData(
    id int not null primary key,
    age_range varchar(255) not null,
    ethinicity_id int,
    outcome_linked_to_object_of_search boolean not null,
    date_of_operation datetime not null,
    removal_of_more_than_outer_clothing boolean not null,
    operation boolean not null,
    officer_defined_ethnicity varchar(255),
    search_objective_id int,
    involved_person boolean not null,
    gender varchar(10) not null,
    legislation_id int,
    location_id int,
    outcome_id int,
    search_type_id int,
    operation_id int,
    ethinicity_id int FOREIGN KEY REFERENCES Ethnicity(id),
    search_objective_id int FOREIGN KEY REFERENCES SearchObjective(id),
    legislation_id int FOREIGN KEY REFERENCES Legislation(id),
    location_id int FOREIGN KEY REFERENCES Location(id),
    outcome_id int FOREIGN KEY REFERENCES Outcome(id),
    operation_id int FOREIGN KEY REFERENCES Operation(id)
);