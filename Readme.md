
# ViewSets:

+ ViewSets works exactly same as generic views(CBV). The only difference is that 
it allows us to combine the logic for set of related views in a single class.

+ It does not provide method handlers like "get", "post", "put", etc.

+ We do not configure the urls with ViewSets instead we use Routers to register viewsets.

+ Routers generates urls for ViewSets automatically  and binds methods like "retrieve", "list", 
"create", "update", "delete", "partial_upate" for different request method types(GET, POST, etc).

### DRF provides three generic viewsets GenericViewSet, ReadOnlyModelViewSet, ModelViewSet

## GenericViewSet:

+ It does not include the basic actions/methods like "list", "create", etc. we have to define these methods  in order to use it.
+ But It provides methods like "get_object" and "get_queryset"

+ Inherit it and use it only if you want to implement completly new behaviour rather than the basic behaviour provided by DRF.


## ReadOnlyModelViewSet:
+ It provides the functionality of CBV views ListAPIView and RetrieveAPIView in a single class.

+ It accepts only accepts the request method type "GET"

## ModelViewSet:

+ It provides complete functionality of CBV of DRF in a single class.

+ You can avoid writing of six different classes.

+ You can also avoid configuring of urls for classes.