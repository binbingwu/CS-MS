import java.util.*;

abstract class NamedData {
    private String name;

    public NamedData( String aName ) {
        name = aName;
    }

    public String getName() {
        return name;
    }
}

class WayPoint extends NamedData {
    private Location location;

    public WayPoint( String aName, Location aLocation ) {
        super( aName );
        location = aLocation;
    }
}

class Track extends NamedData {
    private Location[] locations;

    public Track( String aName ) {
        super( aName );
        locations = new Location[10000];
    }
}

class Trip extends NamedData {
    private ArrayList<NamedData> collection;

    public Trip( String aName ) {
        super( aName );
        collection = new ArrayList<NamedData>();
    }

    public void add( NamedData aNamedData ) {
        if (! collection.contains( aNamedData )) {
            collection.add( aNamedData );
        }
    }
}

class Location {
    private String latitude;
    private String longitude;

    public Location( String aLatitude, String aLongitude ) {
        latitude = aLatitude;
        longitude = aLongitude;
    }
}
