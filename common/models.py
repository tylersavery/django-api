import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):

    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4(),
        unique=True,
        editable=False,
        db_index=True,
    )

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
